QT += network

HEADERS += \
# Models
    $${PWD}/OAIAddress.h \
    $${PWD}/OAIProfile.h \
    $${PWD}/OAISchema.h \
    $${PWD}/OAISchema_properties.h \
    $${PWD}/OAISchema_properties__fieldName_.h \
    $${PWD}/OAIUpdateClientAddress_request.h \
    $${PWD}/OAIUpdateClientProfile_request.h \
# APIs
    $${PWD}/OAIAddressesApi.h \
    $${PWD}/OAIProfilesApi.h \
    $${PWD}/OAIProspectsApi.h \
    $${PWD}/OAIPurchaseInformationApi.h \
    $${PWD}/OAISchemasApi.h \
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
    $${PWD}/OAIProfile.cpp \
    $${PWD}/OAISchema.cpp \
    $${PWD}/OAISchema_properties.cpp \
    $${PWD}/OAISchema_properties__fieldName_.cpp \
    $${PWD}/OAIUpdateClientAddress_request.cpp \
    $${PWD}/OAIUpdateClientProfile_request.cpp \
# APIs
    $${PWD}/OAIAddressesApi.cpp \
    $${PWD}/OAIProfilesApi.cpp \
    $${PWD}/OAIProspectsApi.cpp \
    $${PWD}/OAIPurchaseInformationApi.cpp \
    $${PWD}/OAISchemasApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
