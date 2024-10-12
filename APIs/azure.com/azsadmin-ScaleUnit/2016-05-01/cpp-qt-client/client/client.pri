QT += network

HEADERS += \
# Models
    $${PWD}/OAICreateFromJsonScaleUnitParametersList.h \
    $${PWD}/OAIDeploymentJsonPhysicalNodeParameters.h \
    $${PWD}/OAINetworkDefinitionParameter.h \
    $${PWD}/OAIScaleOutScaleUnitParameters.h \
    $${PWD}/OAIScaleOutScaleUnitParametersList.h \
    $${PWD}/OAIScaleUnit.h \
    $${PWD}/OAIScaleUnitCapacity.h \
    $${PWD}/OAIScaleUnitList.h \
    $${PWD}/OAIScaleUnitModel.h \
# APIs
    $${PWD}/OAIScaleUnitsApi.h \
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
    $${PWD}/OAICreateFromJsonScaleUnitParametersList.cpp \
    $${PWD}/OAIDeploymentJsonPhysicalNodeParameters.cpp \
    $${PWD}/OAINetworkDefinitionParameter.cpp \
    $${PWD}/OAIScaleOutScaleUnitParameters.cpp \
    $${PWD}/OAIScaleOutScaleUnitParametersList.cpp \
    $${PWD}/OAIScaleUnit.cpp \
    $${PWD}/OAIScaleUnitCapacity.cpp \
    $${PWD}/OAIScaleUnitList.cpp \
    $${PWD}/OAIScaleUnitModel.cpp \
# APIs
    $${PWD}/OAIScaleUnitsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
