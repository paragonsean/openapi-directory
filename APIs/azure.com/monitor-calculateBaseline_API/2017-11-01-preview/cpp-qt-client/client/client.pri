QT += network

HEADERS += \
# Models
    $${PWD}/OAIBaseline.h \
    $${PWD}/OAICalculateBaselineResponse.h \
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAITimeSeriesInformation.h \
# APIs
    $${PWD}/OAIBaselineApi.h \
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
    $${PWD}/OAIBaseline.cpp \
    $${PWD}/OAICalculateBaselineResponse.cpp \
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAITimeSeriesInformation.cpp \
# APIs
    $${PWD}/OAIBaselineApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
