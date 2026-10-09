from src.scilint.unit.scale import Scale


class Dimension:
    def __init__(
        self, scales: dict[str, Scale] | None = None, base_scale: Scale | None = None
    ):
        self.scales = scales
        self.base_scale = base_scale

    def __init_subclass__(cls, **kwargs):
        super().__init__(**kwargs)
        cls.scales = {}
        cls.base_scale = None

    @classmethod
    def add_scale(cls, scale: Scale, *, is_base: bool = False) -> Scale:
        if scale.name in cls.scales:
            raise ValueError(f"{cls.__name__} already has scale {scale.name}")
        cls.scales[scale.name] = scale
        if is_base or cls.base_scale is None:
            cls.base_scale = scale
        return scale

    @classmethod
    def get_scale(cls, name: str) -> Scale:
        scale = cls.scales.get(name)
        if not scale:
            raise KeyError(f"{cls.__name__} has no scale {name}")
        return scale

    @classmethod
    def convert(
        cls, scale_1: str, scale_2: str, value: float, power: float = 1.0
    ) -> float:
        a, b = cls.get_scale(scale_1), cls.get_scale(scale_2)
        return b.from_base(a.to_base(value))
