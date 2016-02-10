package controller;
import java.util.*;

/**
 * Created by gavin on 10/02/2016.
 */
public class Crap {
    public static void main(String[] args){
        args = args[0].split(";");
        int round = Integer.parseInt(args[0]);
        String playerId = args[1];
        String[] stats;
        for(int i=2;i < args.length;i++){
            String[] playerArgs = args[i].split("_");
            String id = playerArgs[0];
            if(id.equals(playerId)){
                stats = playerArgs;
                System.err.println(args[i]);
            }
        }



        System.out.println("NNN");
    }
}
