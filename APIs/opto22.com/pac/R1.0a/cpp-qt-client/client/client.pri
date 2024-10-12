QT += network

HEADERS += \
# Models
    $${PWD}/OAIControllerResponse.h \
    $${PWD}/OAIDigitalPointStateObject.h \
    $${PWD}/OAIDigitalPointStateVar.h \
    $${PWD}/OAIErrorResponse200OKish.h \
    $${PWD}/OAIErrorResponse400BadAdminOrValue.h \
    $${PWD}/OAIErrorResponse401BadKeyForBasicAuth.h \
    $${PWD}/OAIErrorResponse404NotFound.h \
    $${PWD}/OAIFloatValueObject.h \
    $${PWD}/OAIFloatVar.h \
    $${PWD}/OAIInt32ValueObject.h \
    $${PWD}/OAIInt32Var.h \
    $${PWD}/OAIInt64StringValueObject.h \
    $${PWD}/OAIInt64ValueObject.h \
    $${PWD}/OAIInt64Var.h \
    $${PWD}/OAIInt64VarAsString.h \
    $${PWD}/OAIStrategyResponse.h \
    $${PWD}/OAIStringValueObject.h \
    $${PWD}/OAIStringVar.h \
    $${PWD}/OAITableDef.h \
# APIs
    $${PWD}/OAIAllApi.h \
    $${PWD}/OAIDeviceApi.h \
    $${PWD}/OAIIosApi.h \
    $${PWD}/OAIStrategyApi.h \
    $${PWD}/OAITablesApi.h \
    $${PWD}/OAIVarsApi.h \
# Others
    $${PWD}/OAIHelpers.h \
    $${PWD}/OAIHttpRequest.h \
    $${PWD}/OAIObject.h \
    $${PWD}/OAIEnum.h \
    $${PWD}/OAIHttpFileElement.h \
    $${PWD}/OAIServerConfiguration.h \
    $${PWD}/OAIServerVariable.h \
    $${PWD}/OAIOauth.h

SOURCES += \
# Models
    $${PWD}/OAIControllerResponse.cpp \
    $${PWD}/OAIDigitalPointStateObject.cpp \
    $${PWD}/OAIDigitalPointStateVar.cpp \
    $${PWD}/OAIErrorResponse200OKish.cpp \
    $${PWD}/OAIErrorResponse400BadAdminOrValue.cpp \
    $${PWD}/OAIErrorResponse401BadKeyForBasicAuth.cpp \
    $${PWD}/OAIErrorResponse404NotFound.cpp \
    $${PWD}/OAIFloatValueObject.cpp \
    $${PWD}/OAIFloatVar.cpp \
    $${PWD}/OAIInt32ValueObject.cpp \
    $${PWD}/OAIInt32Var.cpp \
    $${PWD}/OAIInt64StringValueObject.cpp \
    $${PWD}/OAIInt64ValueObject.cpp \
    $${PWD}/OAIInt64Var.cpp \
    $${PWD}/OAIInt64VarAsString.cpp \
    $${PWD}/OAIStrategyResponse.cpp \
    $${PWD}/OAIStringValueObject.cpp \
    $${PWD}/OAIStringVar.cpp \
    $${PWD}/OAITableDef.cpp \
# APIs
    $${PWD}/OAIAllApi.cpp \
    $${PWD}/OAIDeviceApi.cpp \
    $${PWD}/OAIIosApi.cpp \
    $${PWD}/OAIStrategyApi.cpp \
    $${PWD}/OAITablesApi.cpp \
    $${PWD}/OAIVarsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
