QT += network

HEADERS += \
# Models
    $${PWD}/OAIAtomisedName.h \
    $${PWD}/OAIClientStatus.h \
    $${PWD}/OAIHigherClassificationElement.h \
    $${PWD}/OAIOtherNames.h \
    $${PWD}/OAIQuery.h \
    $${PWD}/OAIRequest.h \
    $${PWD}/OAIResponse.h \
    $${PWD}/OAIServiceProviderInfo.h \
    $${PWD}/OAISource.h \
    $${PWD}/OAISynonym.h \
    $${PWD}/OAITaxon.h \
    $${PWD}/OAITaxonName.h \
    $${PWD}/OAITnrMsg.h \
# APIs
    $${PWD}/OAIUtisControllerApi.h \
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
    $${PWD}/OAIAtomisedName.cpp \
    $${PWD}/OAIClientStatus.cpp \
    $${PWD}/OAIHigherClassificationElement.cpp \
    $${PWD}/OAIOtherNames.cpp \
    $${PWD}/OAIQuery.cpp \
    $${PWD}/OAIRequest.cpp \
    $${PWD}/OAIResponse.cpp \
    $${PWD}/OAIServiceProviderInfo.cpp \
    $${PWD}/OAISource.cpp \
    $${PWD}/OAISynonym.cpp \
    $${PWD}/OAITaxon.cpp \
    $${PWD}/OAITaxonName.cpp \
    $${PWD}/OAITnrMsg.cpp \
# APIs
    $${PWD}/OAIUtisControllerApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
