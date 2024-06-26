import java.util.concurrent.ThreadLocalRandom;


public class FridgeContext{
    private FridgeState state;
    private String brand;

    public void setState(FridgeState newState){
        state = newState;
        System.out.println("The " + brand + " fridge state changed");
    }

    public FridgeContext(String initialBrand){
        brand = initialBrand;
    }

    public double getTemperature(){
        return state.getBaseTemperature()
        + ThreadLocalRandom.current().nextDouble() * 4  - 2.0;
    }

    public void printTemperature(){
        System.out.println("The " + brand + " fridge temperature: " + this.getTemperature());
    }

    public void executeStateActions(){
        state.doStateActions();
    }

}
