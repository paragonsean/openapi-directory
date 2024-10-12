QT += network

HEADERS += \
# Models
    $${PWD}/OAIComputeFlightEmissionsRequest.h \
    $${PWD}/OAIComputeFlightEmissionsResponse.h \
    $${PWD}/OAIDate.h \
    $${PWD}/OAIEmissionsGramsPerPax.h \
    $${PWD}/OAIFlight.h \
    $${PWD}/OAIFlightWithEmissions.h \
    $${PWD}/OAIModelVersion.h \
# APIs
    $${PWD}/OAIFlightsApi.h \
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
    $${PWD}/OAIComputeFlightEmissionsRequest.cpp \
    $${PWD}/OAIComputeFlightEmissionsResponse.cpp \
    $${PWD}/OAIDate.cpp \
    $${PWD}/OAIEmissionsGramsPerPax.cpp \
    $${PWD}/OAIFlight.cpp \
    $${PWD}/OAIFlightWithEmissions.cpp \
    $${PWD}/OAIModelVersion.cpp \
# APIs
    $${PWD}/OAIFlightsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
