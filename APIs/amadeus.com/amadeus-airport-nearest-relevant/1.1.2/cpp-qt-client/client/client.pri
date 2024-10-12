QT += network

HEADERS += \
# Models
    $${PWD}/OAIAddress.h \
    $${PWD}/OAIAnalytics.h \
    $${PWD}/OAICollectionLinks.h \
    $${PWD}/OAICollection_Meta.h \
    $${PWD}/OAIDistance.h \
    $${PWD}/OAIError_400.h \
    $${PWD}/OAIError_500.h \
    $${PWD}/OAIFlights.h \
    $${PWD}/OAIGeoCode.h \
    $${PWD}/OAIIssue.h \
    $${PWD}/OAIIssue_Source.h \
    $${PWD}/OAILocation.h \
    $${PWD}/OAISuccess.h \
    $${PWD}/OAITravelers.h \
# APIs
    $${PWD}/OAILocationApi.h \
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
    $${PWD}/OAIAddress.cpp \
    $${PWD}/OAIAnalytics.cpp \
    $${PWD}/OAICollectionLinks.cpp \
    $${PWD}/OAICollection_Meta.cpp \
    $${PWD}/OAIDistance.cpp \
    $${PWD}/OAIError_400.cpp \
    $${PWD}/OAIError_500.cpp \
    $${PWD}/OAIFlights.cpp \
    $${PWD}/OAIGeoCode.cpp \
    $${PWD}/OAIIssue.cpp \
    $${PWD}/OAIIssue_Source.cpp \
    $${PWD}/OAILocation.cpp \
    $${PWD}/OAISuccess.cpp \
    $${PWD}/OAITravelers.cpp \
# APIs
    $${PWD}/OAILocationApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
