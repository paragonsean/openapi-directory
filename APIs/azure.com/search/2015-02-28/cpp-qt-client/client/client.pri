QT += network

HEADERS += \
# Models
    $${PWD}/OAIAdminKeyResult.h \
    $${PWD}/OAIListQueryKeysResult.h \
    $${PWD}/OAIQueryKey.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAISearchServiceCreateOrUpdateParameters.h \
    $${PWD}/OAISearchServiceListResult.h \
    $${PWD}/OAISearchServiceProperties.h \
    $${PWD}/OAISearchServiceReadableProperties.h \
    $${PWD}/OAISearchServiceResource.h \
    $${PWD}/OAISku.h \
    $${PWD}/OAISubResource.h \
# APIs
    $${PWD}/OAIAdminKeysApi.h \
    $${PWD}/OAIQueryKeysApi.h \
    $${PWD}/OAIServicesApi.h \
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
    $${PWD}/OAIAdminKeyResult.cpp \
    $${PWD}/OAIListQueryKeysResult.cpp \
    $${PWD}/OAIQueryKey.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAISearchServiceCreateOrUpdateParameters.cpp \
    $${PWD}/OAISearchServiceListResult.cpp \
    $${PWD}/OAISearchServiceProperties.cpp \
    $${PWD}/OAISearchServiceReadableProperties.cpp \
    $${PWD}/OAISearchServiceResource.cpp \
    $${PWD}/OAISku.cpp \
    $${PWD}/OAISubResource.cpp \
# APIs
    $${PWD}/OAIAdminKeysApi.cpp \
    $${PWD}/OAIQueryKeysApi.cpp \
    $${PWD}/OAIServicesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
