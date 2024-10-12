QT += network

HEADERS += \
# Models
    $${PWD}/OAIAddress.h \
    $${PWD}/OAICharityOrg.h \
    $${PWD}/OAICharitySearchResponse.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorParameter.h \
    $${PWD}/OAIGeoCoordinates.h \
    $${PWD}/OAIImage.h \
    $${PWD}/OAILocation.h \
# APIs
    $${PWD}/OAICharityOrgApi.h \
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
    $${PWD}/OAICharityOrg.cpp \
    $${PWD}/OAICharitySearchResponse.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorParameter.cpp \
    $${PWD}/OAIGeoCoordinates.cpp \
    $${PWD}/OAIImage.cpp \
    $${PWD}/OAILocation.cpp \
# APIs
    $${PWD}/OAICharityOrgApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
