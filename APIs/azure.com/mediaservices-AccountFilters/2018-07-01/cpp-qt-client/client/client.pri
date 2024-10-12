QT += network

HEADERS += \
# Models
    $${PWD}/OAIAccountFilter.h \
    $${PWD}/OAIAccountFilterCollection.h \
    $${PWD}/OAIApiError.h \
    $${PWD}/OAIFilterTrackPropertyCondition.h \
    $${PWD}/OAIFilterTrackSelection.h \
    $${PWD}/OAIFirstQuality.h \
    $${PWD}/OAIMediaFilterProperties.h \
    $${PWD}/OAIODataError.h \
    $${PWD}/OAIPresentationTimeRange.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
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
    $${PWD}/OAIAccountFilter.cpp \
    $${PWD}/OAIAccountFilterCollection.cpp \
    $${PWD}/OAIApiError.cpp \
    $${PWD}/OAIFilterTrackPropertyCondition.cpp \
    $${PWD}/OAIFilterTrackSelection.cpp \
    $${PWD}/OAIFirstQuality.cpp \
    $${PWD}/OAIMediaFilterProperties.cpp \
    $${PWD}/OAIODataError.cpp \
    $${PWD}/OAIPresentationTimeRange.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
