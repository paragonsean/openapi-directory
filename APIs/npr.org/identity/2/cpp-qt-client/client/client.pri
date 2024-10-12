QT += network

HEADERS += \
# Models
    $${PWD}/OAIAbstractCDocLink.h \
    $${PWD}/OAIAbstractLink.h \
    $${PWD}/OAIAffiliation.h \
    $${PWD}/OAIAlgolia.h \
    $${PWD}/OAICohort.h \
    $${PWD}/OAICollectionDocument.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIErrorDocument.h \
    $${PWD}/OAIOrganization.h \
    $${PWD}/OAIUserData.h \
    $${PWD}/OAIUserDocument.h \
# APIs
    $${PWD}/OAIIdentityApi.h \
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
    $${PWD}/OAIAbstractCDocLink.cpp \
    $${PWD}/OAIAbstractLink.cpp \
    $${PWD}/OAIAffiliation.cpp \
    $${PWD}/OAIAlgolia.cpp \
    $${PWD}/OAICohort.cpp \
    $${PWD}/OAICollectionDocument.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIErrorDocument.cpp \
    $${PWD}/OAIOrganization.cpp \
    $${PWD}/OAIUserData.cpp \
    $${PWD}/OAIUserDocument.cpp \
# APIs
    $${PWD}/OAIIdentityApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
