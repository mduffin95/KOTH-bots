import java.util.ArrayList;
import java.util.List;

public class TestBot1 {

	int round;
	int phase;
	int playerID;
	int thisTownID;

	
	List<State> states;
    List<State> otherStates;

    State thisState;
	
    public static void main(String[] args){
        new TestBot1().sleep(args[0].split(";"));
    }
    
    private void sleep(String[] args) {
    	
    	round = Integer.parseInt(args[0]);
		thisTownID = Integer.parseInt(args[1]);
		
		states = new ArrayList<>();
		otherStates = new ArrayList<>();
		
        for (int i = 2; i < args.length; i++){
        	states.add(new State(args[i]));
        }

        for (State state : states){
            if (state.isMine()) {
            	thisState = state;
            } else {
                otherStates.add(state);
            }
        }
        if (round == 50){
            System.out.println("CCC");
            return;
        }
        if (round < 10){
            System.out.println("VVO");
            return;
        }
        if (round < 20){
            System.out.println("CVV");
            return;
        }
        if (round < 30){
            System.out.println("CCV");
            return;
        }
        if (round < 40){
            System.out.println("BQC");
            return;
        }
        if (round < 50){
            System.out.println("BWC");
            return;
        }    
       
    }
    
    private class State {
		 
        private final int ownerId;
        public int healthy;
        public int infected;
        public int dead;
        public int infectionRate;
        public int contagionRate;
        public int lethalityRate;
        public int migrationRate;

        public State(String string) {
            String[] args = string.split("_");
            ownerId = Integer.parseInt(args[0]);
            healthy = Integer.parseInt(args[1]);
            infected = Integer.parseInt(args[2]);
            dead = Integer.parseInt(args[3]);
            infectionRate = Integer.parseInt(args[4]);
            contagionRate = Integer.parseInt(args[5]);
            lethalityRate = Integer.parseInt(args[6]);
            migrationRate = Integer.parseInt(args[7]);
        }
        
        public int getOwnerId() {
			return ownerId;
		}

		public boolean isMine(){
            return getOwnerId() == playerID;
        }

    }

}
