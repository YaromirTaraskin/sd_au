public class UsualChairToTableAdapter implements Table{
    usualChair UsualChair;

    public UsualChairToTableAdapter(UsualChair initialUsualChair) {
        UsualChair = initialUsualChair;
    }

    public providePlaceForThings() {
        UsualChair.provideSittingPalce();
    }
}