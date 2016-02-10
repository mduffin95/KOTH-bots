package players;

import controller.Player;

public class Zombiebot extends Player {

	@Override
	public String getCmd() {
		return "python zombiebot.py";
	}
}
