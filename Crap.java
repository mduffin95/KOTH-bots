//package controller;
import java.util.*;
import java.net.*;

/**
 * Created by gavin on 10/02/2016.
 */
public class Crap {
    public static void main(String[] args){
        args = args[0].split(";");
        int round = Integer.parseInt(args[0]);
        String playerId = args[1];
        String[] stats = args;
        for(int i=2;i < args.length;i++){
            String[] playerArgs = args[i].split("_");
            String id = playerArgs[0];
            if(id.equals(playerId)){
                stats = playerArgs;
                //System.err.println(args[i]);
            }
        }
        int healthy = Integer.parseInt(stats[1]);
        int infected = Integer.parseInt(stats[2]);
        int dead = Integer.parseInt(stats[3]);
        int iRate = Integer.parseInt(stats[4]);
        int cRate = Integer.parseInt(stats[5]);
        int lRate = Integer.parseInt(stats[6]);
        int mRate = Integer.parseInt(stats[7]);
        String out = "";
        if(round == 1){
            out = out + "B";
        }else {
            if (lRate > cRate) {
                out = out + "I";
            } else {
                out = out + "E";
            }
        }
        out = out + "C";
        out = out + "M";
        System.out.println(out);
        try {
            String req = "http://192.168.0.24:8080/?healthy=" + healthy + "&infected=" + infected + "&dead=" + dead;
            URL url = new URL(req);
            URLConnection uc = url.openConnection();
            //uc.setRequestProperty("stats",  Arrays.toString(stats));
            uc.getInputStream();
        }catch(Exception e){
            System.err.println(e);
        }

        return;
    }
}
