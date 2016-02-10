import java.util.ArrayList;
import java.util.List;

public class LifeIsCruel {

	int round;
	int phase;
	int playerID;
	int thisTownID;

	
	List<State> states;
    List<State> otherStates;

    State thisState;
	
    public static void main(String[] args){
        new LifeIsCruel().sleep(args[0].split(";"));
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

        String action = ""; 
        
        action +="W";
        
        if (round == 50){
            System.out.println("CCC");
            return;
        }
        else if (thisState.migrationRate>0){
            action +="B";
        }
        while(action.length()<3){
            if (thisState.infected >= 25 && action.length()<2){
                action +="Q";
                thisState.infected -=30;
            }
            else if (thisState.infected>=5 && action.length()<2){
                action +="C";
                thisState.infected -=10;
                thisState.healthy += 10;
            }
            else if (round%2 == 0){
                action +="M";
            }
            else{
                action +="E";
            }
    
    

       System.out.println(action); 
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
