QT += network

HEADERS += \
# Models
    $${PWD}/OAIFabricLocation.h \
    $${PWD}/OAIFabricLocationList.h \
    $${PWD}/OAIFabricLocationModel.h \
# APIs
    $${PWD}/OAIFabricLocationsApi.h \
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
    $${PWD}/OAIFabricLocation.cpp \
    $${PWD}/OAIFabricLocationList.cpp \
    $${PWD}/OAIFabricLocationModel.cpp \
# APIs
    $${PWD}/OAIFabricLocationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
