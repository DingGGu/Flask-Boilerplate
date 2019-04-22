from config.base import BaseConfig


class AppConfig:
    def __init__(self):
        self._wrapped: BaseConfig = None

    def set_config(self, config_obj: BaseConfig):
        if self._wrapped:
            raise RuntimeError("config already set")

        self._wrapped = config_obj

    def __getattr__(self, name):
        if name == '_wrapped':
            return super().__getattribute__(name)

        if self._wrapped is None:
            raise ValueError("config is not ready!")

        return getattr(self._wrapped, name)

    def __setattr__(self, name, value):
        if not name == '_wrapped':
            raise AttributeError("You can't set a read-only attribute")
        else:
            super().__setattr__(name, value)

    def __dir__(self):  # Support Flask.Config.from_object()
        return dir(self._wrapped)

    def __repr__(self):
        return "<AppConfig of {!r}>".format(self._wrapped)


config = AppConfig()
