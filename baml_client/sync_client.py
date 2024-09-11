###############################################################################
#
#  Welcome to Baml! To use this generated code, please run the following:
#
#  $ pip install baml
#
###############################################################################

# This file was generated by BAML: please do not edit it. Instead, edit the
# BAML files and re-generate this code.
#
# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off
from typing import Any, Dict, List, Optional, TypeVar, Union, TypedDict, Type
from typing_extensions import NotRequired
import pprint

import baml_py
from pydantic import BaseModel, ValidationError, create_model

from . import partial_types, types
from .type_builder import TypeBuilder
from .globals import DO_NOT_USE_DIRECTLY_UNLESS_YOU_KNOW_WHAT_YOURE_DOING_CTX, DO_NOT_USE_DIRECTLY_UNLESS_YOU_KNOW_WHAT_YOURE_DOING_RUNTIME

OutputType = TypeVar('OutputType')

def coerce(cls: Type[BaseModel], parsed: Any) -> Any:
  try:
    return cls.model_validate({"inner": parsed}).inner # type: ignore
  except ValidationError as e:
    raise TypeError(
      "Internal BAML error while casting output to {}\n{}".format(
        cls.__name__,
        pprint.pformat(parsed)
      )
    ) from e

# Define the TypedDict with optional parameters having default values
class BamlCallOptions(TypedDict, total=False):
    tb: NotRequired[TypeBuilder]
    client_registry: NotRequired[baml_py.baml_py.ClientRegistry]

class BamlSyncClient:
    __runtime: baml_py.BamlRuntime
    __ctx_manager: baml_py.BamlCtxManager
    __stream_client: "BamlStreamClient"

    def __init__(self, runtime: baml_py.BamlRuntime, ctx_manager: baml_py.BamlCtxManager):
      self.__runtime = runtime
      self.__ctx_manager = ctx_manager
      self.__stream_client = BamlStreamClient(self.__runtime, self.__ctx_manager)

    @property
    def stream(self):
      return self.__stream_client

    
    def ExtractMessageCategoryFromMessage(
        self,
        message: str,
        baml_options: BamlCallOptions = {},
    ) -> types.HarmfulMessageCategory:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.call_function_sync(
        "ExtractMessageCategoryFromMessage",
        {
          "message": message,
        },
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )
      mdl = create_model("ExtractMessageCategoryFromMessageReturnType", inner=(types.HarmfulMessageCategory, ...))
      return coerce(mdl, raw.parsed())
    
    def ExtractResume(
        self,
        resume: str,
        baml_options: BamlCallOptions = {},
    ) -> types.Resume:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.call_function_sync(
        "ExtractResume",
        {
          "resume": resume,
        },
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )
      mdl = create_model("ExtractResumeReturnType", inner=(types.Resume, ...))
      return coerce(mdl, raw.parsed())
    
    def IdentifyHarmfulDiscordMessage(
        self,
        discord_message: str,
        baml_options: BamlCallOptions = {},
    ) -> types.IsHarmfulMessage:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.call_function_sync(
        "IdentifyHarmfulDiscordMessage",
        {
          "discord_message": discord_message,
        },
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )
      mdl = create_model("IdentifyHarmfulDiscordMessageReturnType", inner=(types.IsHarmfulMessage, ...))
      return coerce(mdl, raw.parsed())
    



class BamlStreamClient:
    __runtime: baml_py.BamlRuntime
    __ctx_manager: baml_py.BamlCtxManager

    def __init__(self, runtime: baml_py.BamlRuntime, ctx_manager: baml_py.BamlCtxManager):
      self.__runtime = runtime
      self.__ctx_manager = ctx_manager

    
    def ExtractMessageCategoryFromMessage(
        self,
        message: str,
        baml_options: BamlCallOptions = {},
    ) -> baml_py.BamlSyncStream[Optional[types.HarmfulMessageCategory], types.HarmfulMessageCategory]:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.stream_function_sync(
        "ExtractMessageCategoryFromMessage",
        {
          "message": message,
        },
        None,
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )

      mdl = create_model("ExtractMessageCategoryFromMessageReturnType", inner=(types.HarmfulMessageCategory, ...))
      partial_mdl = create_model("ExtractMessageCategoryFromMessagePartialReturnType", inner=(Optional[types.HarmfulMessageCategory], ...))

      return baml_py.BamlSyncStream[Optional[types.HarmfulMessageCategory], types.HarmfulMessageCategory](
        raw,
        lambda x: coerce(partial_mdl, x),
        lambda x: coerce(mdl, x),
        self.__ctx_manager.get(),
      )
    
    def ExtractResume(
        self,
        resume: str,
        baml_options: BamlCallOptions = {},
    ) -> baml_py.BamlSyncStream[partial_types.Resume, types.Resume]:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.stream_function_sync(
        "ExtractResume",
        {
          "resume": resume,
        },
        None,
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )

      mdl = create_model("ExtractResumeReturnType", inner=(types.Resume, ...))
      partial_mdl = create_model("ExtractResumePartialReturnType", inner=(partial_types.Resume, ...))

      return baml_py.BamlSyncStream[partial_types.Resume, types.Resume](
        raw,
        lambda x: coerce(partial_mdl, x),
        lambda x: coerce(mdl, x),
        self.__ctx_manager.get(),
      )
    
    def IdentifyHarmfulDiscordMessage(
        self,
        discord_message: str,
        baml_options: BamlCallOptions = {},
    ) -> baml_py.BamlSyncStream[partial_types.IsHarmfulMessage, types.IsHarmfulMessage]:
      __tb__ = baml_options.get("tb", None)
      if __tb__ is not None:
        tb = __tb__._tb
      else:
        tb = None
      __cr__ = baml_options.get("client_registry", None)

      raw = self.__runtime.stream_function_sync(
        "IdentifyHarmfulDiscordMessage",
        {
          "discord_message": discord_message,
        },
        None,
        self.__ctx_manager.get(),
        tb,
        __cr__,
      )

      mdl = create_model("IdentifyHarmfulDiscordMessageReturnType", inner=(types.IsHarmfulMessage, ...))
      partial_mdl = create_model("IdentifyHarmfulDiscordMessagePartialReturnType", inner=(partial_types.IsHarmfulMessage, ...))

      return baml_py.BamlSyncStream[partial_types.IsHarmfulMessage, types.IsHarmfulMessage](
        raw,
        lambda x: coerce(partial_mdl, x),
        lambda x: coerce(mdl, x),
        self.__ctx_manager.get(),
      )
    

b = BamlSyncClient(DO_NOT_USE_DIRECTLY_UNLESS_YOU_KNOW_WHAT_YOURE_DOING_RUNTIME, DO_NOT_USE_DIRECTLY_UNLESS_YOU_KNOW_WHAT_YOURE_DOING_CTX)

__all__ = ["b"]