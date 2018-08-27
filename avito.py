class Ad:
    id: int = None

    def __init__(self, ad_id):
        self.id = ad_id


class Car(Ad):
    mark: str = None
    model: str = None
    release_year: int = None
    mileage: int = None
    condition: str = None
    vin: str = None
    body_type: str = None
    num_of_doors: int = None
    color: str = None
    engines_type: str = None
    engine_capacity: str = None
    transmission: str = None
    drive: str = None
    helm: str = None
    num_of_owners: int = None
    description: str = None
    price: int = None
    address: str = None

    def __init__(self, ad_id, car_type):
        Ad.__init__(self, ad_id)
        self.type = car_type
