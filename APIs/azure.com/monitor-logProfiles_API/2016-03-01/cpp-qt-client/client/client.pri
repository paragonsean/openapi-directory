QT += network

HEADERS += \
# Models
    $${PWD}/OAIErrorResponse.h \
    $${PWD}/OAILogProfileCollection.h \
    $${PWD}/OAILogProfileProperties.h \
    $${PWD}/OAILogProfileResource.h \
    $${PWD}/OAILogProfileResourcePatch.h \
    $${PWD}/OAIResource.h \
    $${PWD}/OAIRetentionPolicy.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
    $${PWD}/OAILogProfilesApi.h \
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
    $${PWD}/OAIErrorResponse.cpp \
    $${PWD}/OAILogProfileCollection.cpp \
    $${PWD}/OAILogProfileProperties.cpp \
    $${PWD}/OAILogProfileResource.cpp \
    $${PWD}/OAILogProfileResourcePatch.cpp \
    $${PWD}/OAIResource.cpp \
    $${PWD}/OAIRetentionPolicy.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
    $${PWD}/OAILogProfilesApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
