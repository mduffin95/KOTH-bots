package players;

import controller.Player;

public class Insight extends Player {

	@Override
	public String getCmd() {
		return "python3 insight.py";
	}

}
