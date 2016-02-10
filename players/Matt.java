package players;

import controller.Player;

public class Matt extends Player {

	@Override
	public String getCmd() {
		return "python3 matt.py";
	}

}
