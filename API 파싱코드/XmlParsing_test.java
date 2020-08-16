package basic;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;

import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

public class XmlParsing_test {

    // tag값의 정보를 가져오는 메소드
   private static String getTagValue(String tag, Element eElement) {
       NodeList nlList = eElement.getElementsByTagName(tag).item(0).getChildNodes();
       Node nValue = (Node) nlList.item(0);
       if(nValue == null) 
           return null;
       return nValue.getNodeValue();
   }

   public static void main(String[] args) {
      
      int page2 = 10;   // 페이지 초기값
      
      
      
      try{
         while(true){
            // parsing할 url 지정(API 키 포함해서)
            String url = "http://apis.data.go.kr/1470000/MdcinSdefctInfoService/getMdcinSdefctInfoList?serviceKey=mFW3I9zgl4vL6raWIh5QNyRZxIuxHHzVVutLRKteGhUZQnbd%2BYUocob3AsbcP6imSjhZ9FO8TwmdXZFLgVtxpg%3D%3D&numOfRows=3&pageNo="+page2;
            
            DocumentBuilderFactory dbFactoty = DocumentBuilderFactory.newInstance();
            DocumentBuilder dBuilder = dbFactoty.newDocumentBuilder();
            Document doc = dBuilder.parse(url);
            
            // root tag 
            doc.getDocumentElement().normalize();
            System.out.println("Root element :" + doc.getDocumentElement().getNodeName());
            
            // 파싱할 tag
            NodeList nList = doc.getElementsByTagName("item");
            //System.out.println("파싱할 리스트 수 : "+ nList.getLength());
            
            for(int temp = 0; temp < nList.getLength(); temp++){
               Node nNode = nList.item(temp);
               if(nNode.getNodeType() == Node.ELEMENT_NODE){
                  
                  Element eElement = (Element) nNode;
                  System.out.println("######################");
                  //System.out.println(eElement.getTextContent())
                  String a = getTagValue("COL_001", eElement);
                 
                  String c = getTagValue("COL_005", eElement);
                  
                  
                  System.out.println("이름(한글)  : " + a);
                 
                  System.out.println("부작용(한글) : " + c);
               
               
                  
                  List<String> list = new ArrayList<String>();
                  list.add(a);
            
                  list.add(c);
              
                  
                  System.out.println(list.get(0));
                  System.out.println(list.get(1));
           
                  
                     Connection con = null;
                     PreparedStatement pstmt = null;
                     
                     String driver = "com.mysql.jdbc.Driver";
                     String url1 = "jdbc:mysql://localhost:3306/test";
                     String user = "root";
                     String password = "1234";
                     
                     try {
                        Class.forName(driver);
                        con = DriverManager.getConnection(url1, user, password);
                        
                        String sql = "INSERT INTO aaa VALUES (?,?)";
                        pstmt = con.prepareStatement(sql);
                        pstmt.setString(1, list.get(0));
                        pstmt.setString(2, list.get(1));
                 
                        pstmt.executeUpdate(); // INSERT 구문 실행 결과를 int형 변수에 저장
                     } catch (ClassNotFoundException e) {
                        e.printStackTrace();
                     } catch (SQLException e) {
                        e.printStackTrace();
                     } finally {
                        // 자원 반환 => 예외 발생 여부와 관계없이 실행되어야 하므로
                        // finally 블록 내에서 close() 메서드를 호출한다!
                        try {
                           pstmt.close();
                           con.close();
                        } catch (SQLException e) {
                           e.printStackTrace();
                        }
                     }
                     
               
               }   // for end
            }   // if end
            
            page2 += 1;
            
            System.out.println("page number : "+page2);
            if(page2 > 30){
               break;
            }
         }   // while end
         
      } catch (Exception e){   
         e.printStackTrace();
      }   // try~catch end
   }   // main end
}   // class end
