public class FridgeStateCool implements FridgeState {


    private static FridgeStateCool instance = new FridgeStateCool();

    private FridgeStateCool() {}

    public static FridgeState getInstance() {
        return instance;
    }

    @Override
    public double getBaseTemperature() {
        return 12.0;
    }

    public void saveFruits(){
        System.out.println("Fruits were saved");
    }

    public void spoilFish(){
        System.out.println("Fish were spoiled");
    }

    @Override
    public void doStateActions(){
        saveFruits();
        spoilFish();
    }
}
