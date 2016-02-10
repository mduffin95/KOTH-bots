package players;

import controller.Player;

public class Nick extends Player {

	@Override
	public String getCmd() {
		return "python nick.py";
	}

}
