QT += network

HEADERS += \
# Models
    $${PWD}/OAIAgent.h \
    $${PWD}/OAIAssociation.h \
    $${PWD}/OAIBroker.h \
    $${PWD}/OAIContactInformation.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIGeographicData.h \
    $${PWD}/OAIListing.h \
    $${PWD}/OAIMlsInformation.h \
    $${PWD}/OAIOffice.h \
    $${PWD}/OAIOpenHouse.h \
    $${PWD}/OAIParking.h \
    $${PWD}/OAIProperty.h \
    $${PWD}/OAISales.h \
    $${PWD}/OAISchool.h \
    $${PWD}/OAIStreetAddress.h \
    $${PWD}/OAITax.h \
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
    $${PWD}/OAIAgent.cpp \
    $${PWD}/OAIAssociation.cpp \
    $${PWD}/OAIBroker.cpp \
    $${PWD}/OAIContactInformation.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIGeographicData.cpp \
    $${PWD}/OAIListing.cpp \
    $${PWD}/OAIMlsInformation.cpp \
    $${PWD}/OAIOffice.cpp \
    $${PWD}/OAIOpenHouse.cpp \
    $${PWD}/OAIParking.cpp \
    $${PWD}/OAIProperty.cpp \
    $${PWD}/OAISales.cpp \
    $${PWD}/OAISchool.cpp \
    $${PWD}/OAIStreetAddress.cpp \
    $${PWD}/OAITax.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
