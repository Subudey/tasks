class UndergroundSystem():
    def __init__(self):
        self._checked_in = {}
        self._routes = {}

    def check_in(self, passanger_id, station, time):
        if passanger_id in self._checked_in:
            raise ValueError("Пассажир уже вошел")

        self._checked_in[passanger_id] = (station, time)

    def check_out(self, passanger_id, station, time):
        if passanger_id not in self._checked_in:
            raise ValueError("Пассажир еще не вошел")

        start_station, start_time = self._checked_in.pop(passanger_id)

        route = (start_station, station)

        total, count = self._routes.get(route, (0,0))

        self._routes[route] = (total + (time - start_time), count + 1)

    def get_average_time(self, start_station, end_station):
        route = (start_station, end_station)

        if route not in self._routes:
            raise ValueError("Нет данных о маршруте")

        total, count = self._routes[route]

        return total / count
