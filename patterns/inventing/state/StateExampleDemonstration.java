public final class StateExampleDemonstration {
    public static void main(String[] args) {
        FridgeContext FridgeA = new FridgeContext("Azkl");
        FridgeContext FridgeB = new FridgeContext("Banana");

        System.out.println("---");

        FridgeA.setState(FridgeStateCold.getInstance());
        FridgeA.printTemperature();
        FridgeA.executeStateActions();

        System.out.println("---");

        FridgeA.setState(FridgeStateFreezing.getInstance());
        FridgeA.printTemperature();
        FridgeA.executeStateActions();

        System.out.println("---");

        FridgeB.setState(FridgeStateCold.getInstance());
        FridgeB.printTemperature();
        FridgeB.executeStateActions();

        System.out.println("---");

        FridgeA.setState(FridgeStateCool.getInstance());
        FridgeA.printTemperature();
        FridgeA.executeStateActions();

        System.out.println("---");

        FridgeB.setState(FridgeStateFreezing.getInstance());
        FridgeB.printTemperature();
        FridgeB.executeStateActions();

        System.out.println("---");

    }
}
