#!/usr/bin/python3
"""Defines class BaseGeometry."""


class BaseGeometry:
    """Represent a base geometry class."""

    def __getattr__(self, name):
        def fallback(*args, **kwargs):
            raise NotImplementedError(
                "{name} is not implemented {self.__class__.__name__}.".format(
                    name=name, self=self
                )
            )

        return fallback
