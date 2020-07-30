import java.awt.FlowLayout;
import java.awt.Font;
import java.sql.Time;

import javax.swing.JFrame;
import javax.swing.JLabel;

class TimerThread extends Thread{
	
	
	JLabel ttlabel2;
	JLabel ttlabel;
	
	
	
	
	public TimerThread() {}
	public TimerThread(JLabel la , JLabel la2 ) {
		ttlabel = la;		
		ttlabel2 = la2;		
	}
	

	@Override
	public void run() {
		// 0부터 1씩 증가 ~ 무한
		// 해당 라벨에 출력
		// 1초를 기다림(sleep)
		ttlabel2.setText("0");
		int n = 0 ;
		int i = -1 ;
		while(true){
			//ttlabel.setText(Integer.toString(n));
			
			    
				
				for(n=0 ; n<60 ; n++) {
					
					if(n < 10) {
						for(n=0 ; n<10 ;n++) {
							
							if(n == 0) {
								i++;
								ttlabel2.setText(i+"");
							}
						
							try {
								Thread.sleep(200);
							} catch (InterruptedException e) {
								e.printStackTrace();
							}
							ttlabel.setText("0"+n+"");
						}
					}	
							
					ttlabel.setText(n+"");
				
					try {
						Thread.sleep(200);
					} catch (InterruptedException e) {
						e.printStackTrace();
					}
					
					
				}
				
				
			
			
			
		}
	}
	
}



class FrameEx4 extends JFrame{
	
	JLabel la,la2,la3;
	
	public FrameEx4(){
		setTitle("타이머 v1.0");
		
		setLayout(new FlowLayout());
		
		la = new JLabel("0");
		la.setFont(new Font("Gothic", Font.BOLD, 80));
		
		la2 = new JLabel("00");
		la2.setFont(new Font("Gothic", Font.BOLD, 80));
		
		la3 = new JLabel(":");
		la3.setFont(new Font("Gothic", Font.BOLD, 80));
		
		
		this.add(la2);
		this.add(la3);
		this.add(la);
		
		TimerThread tt = new TimerThread(la,la2);
		
		
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		setSize(250,150);
		setVisible(true);
		
		tt.start();
		
		
	}
	
}



public class Test4 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
        new FrameEx4();
	}

}
