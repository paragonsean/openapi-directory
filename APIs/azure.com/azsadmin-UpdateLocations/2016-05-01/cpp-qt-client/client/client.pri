QT += network

HEADERS += \
# Models
    $${PWD}/OAIRegionUpdateState.h \
    $${PWD}/OAIUpdateLocation.h \
    $${PWD}/OAIUpdateLocationList.h \
    $${PWD}/OAIUpdateLocationModel.h \
# APIs
    $${PWD}/OAIUpdateLocationsApi.h \
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
    $${PWD}/OAIRegionUpdateState.cpp \
    $${PWD}/OAIUpdateLocation.cpp \
    $${PWD}/OAIUpdateLocationList.cpp \
    $${PWD}/OAIUpdateLocationModel.cpp \
# APIs
    $${PWD}/OAIUpdateLocationsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
