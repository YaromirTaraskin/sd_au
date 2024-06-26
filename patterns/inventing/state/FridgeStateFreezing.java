public class FridgeStateFreezing implements FridgeState {


    private static FridgeStateFreezing instance = new FridgeStateFreezing();

    private FridgeStateFreezing() {}

    public static FridgeState getInstance() {
        return instance;
    }

    @Override
    public double getBaseTemperature() {
        return -4.0;
    }

    public void freezeWater(){
        System.out.println("The water was freezed");
    }

    @Override
    public void doStateActions(){
        freezeWater();
    }
}
