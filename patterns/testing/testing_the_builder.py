import unittest
import provided_builder


class TestCarBuilder(unittest.TestCase):
    def test_result_is_car(self):
        self.assertIsInstance(
            provided_builder.CarBuilder().getResult(),
            provided_builder.Car
        )

    def test_zero_seats(self):
        # марсоход
        car_builder = provided_builder.CarBuilder()
        car_builder.setSeats(0)
        car = car_builder.getResult()
        self.assertEqual(0, car.seats)

    def test_one_seat(self):
        car_builder = provided_builder.CarBuilder()
        car_builder.setSeats(1)
        car = car_builder.getResult()
        self.assertEqual(1, car.seats)

    def test_some_seats(self):
        some = 4
        car_builder = provided_builder.CarBuilder()
        car_builder.setSeats(some)
        car = car_builder.getResult()
        self.assertEqual(some, car.seats)

    def test_V0_engine(self):
        car_builder = provided_builder.CarBuilder()
        car_builder.setEngine("V0")
        car = car_builder.getResult()
        self.assertEqual("V0", car.engine)

    def test_UE_engine(self):
        car_builder = provided_builder.CarBuilder()
        car_builder.setEngine("Unreal Engine")
        car = car_builder.getResult()
        self.assertEqual("Unreal Engine", car.engine)

    def test_Mystery_engine(self):
        car_builder = provided_builder.CarBuilder()
        car_builder.setEngine("?&;\"Mystery(%#\u3164")
        car = car_builder.getResult()
        self.assertEqual("?&;\"Mystery(%#\u3164", car.engine)

    def test_left_steering_wheel(self):
        car_builder = provided_builder.CarBuilder()
        car_builder.setSteeringWheel("левый")
        car = car_builder.getResult()
        self.assertEqual("левый", car.steering_wheel)

    def test_right_steering_wheel(self):
        car_builder = provided_builder.CarBuilder()
        car_builder.setSteeringWheel("правый")
        car = car_builder.getResult()
        self.assertEqual("правый", car.steering_wheel)

    def test_non_left_steering_wheel(self):
        car_builder = provided_builder.CarBuilder()
        car_builder.setSteeringWheel("не левый")
        car = car_builder.getResult()
        self.assertEqual("не левый", car.steering_wheel)

    def test_middle_steering_wheel(self):
        car_builder = provided_builder.CarBuilder()
        car_builder.setSteeringWheel("средний")
        car = car_builder.getResult()
        self.assertEqual("средний", car.steering_wheel)

    def test_has_gps(self):
        car_builder = provided_builder.CarBuilder()
        car_builder.setGPS(True)
        car = car_builder.getResult()
        self.assertTrue(car.gps)

    def test_has_no_gps(self):
        car_builder = provided_builder.CarBuilder()
        car_builder.setGPS(False)
        car = car_builder.getResult()
        self.assertFalse(car.gps)


class TestCarManualBuilder(unittest.TestCase):
    """"""
    '''
    SetSteeringWheel в принципе реализована странно:
    manual.steering_wheel_description будет "Этот автомобиль левый."
    или "Этот автомобиль правый."
    -- по этой причине setSteeringWheel не тестируется.
    '''

    def test_result_is_manual(self):
        self.assertIsInstance(
            provided_builder.CarManualBuilder().getResult(),
            provided_builder.Manual
        )

    def test_zero_seats(self):
        # марсоход
        manual_builder = provided_builder.CarManualBuilder()
        manual_builder.setSeats(0)
        manual = manual_builder.getResult()
        self.assertEqual("В этом автомобиле 0 мест.", manual.seats_description)

    def test_one_seat(self):
        manual_builder = provided_builder.CarManualBuilder()
        manual_builder.setSeats(1)
        manual = manual_builder.getResult()
        self.assertEqual("В этом автомобиле 1 место.", manual.seats_description)

    def test_2_4_seats(self):
        some = 4
        manual_builder = provided_builder.CarManualBuilder()
        manual_builder.setSeats(some)
        manual = manual_builder.getResult()
        self.assertEqual(f"В этом автомобиле {some} места.", manual.seats_description)

    def test_5_9_seats(self):
        many = 106
        manual_builder = provided_builder.CarManualBuilder()
        manual_builder.setSeats(many)
        manual = manual_builder.getResult()
        self.assertEqual(f"В этом автомобиле {many} мест.", manual.seats_description)

    def test_V0_engine(self):
        manual_builder = provided_builder.CarManualBuilder()
        manual_builder.setEngine("V0")
        manual = manual_builder.getResult()
        self.assertEqual("Этот автомобиль оснащен двигателем V0.", manual.engine_description)

    def test_UE_engine(self):
        manual_builder = provided_builder.CarManualBuilder()
        manual_builder.setEngine("Unreal Engine")
        manual = manual_builder.getResult()
        self.assertEqual(
            "Этот автомобиль оснащен двигателем Unreal Engine.",
            manual.engine_description
        )

    def test_Mystery_engine(self):
        manual_builder = provided_builder.CarManualBuilder()
        manual_builder.setEngine("?&;\"Mystery(%#\u3164")
        manual = manual_builder.getResult()
        self.assertEqual(
            "Этот автомобиль оснащен двигателем ?&;\"Mystery(%#\u3164.",
            manual.engine_description
        )

    def test_has_no_gps(self):
        manual_builder = provided_builder.CarManualBuilder()
        manual_builder.setGPS(False)
        manual = manual_builder.getResult()
        self.assertEqual("Этот автомобиль не оснащен системой GPS.", manual.gps_description)

    def test_has_gps(self):
        manual_builder = provided_builder.CarManualBuilder()
        manual_builder.setGPS(True)
        manual = manual_builder.getResult()
        self.assertEqual("Этот автомобиль оснащен системой GPS.", manual.gps_description)


if __name__ == "__main__":
    unittest.main()
