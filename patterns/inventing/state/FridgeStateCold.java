public class FridgeStateCold implements FridgeState {


    private static FridgeStateCold instance = new FridgeStateCold();

    private FridgeStateCold() {}

    public static FridgeState getInstance() {
        return instance;
    }

    @Override
    public double getBaseTemperature() {
        return 4.0;
    }

    @Override
    public void doStateActions(){
    }
}
