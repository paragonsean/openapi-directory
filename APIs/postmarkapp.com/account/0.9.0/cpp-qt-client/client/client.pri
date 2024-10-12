QT += network

HEADERS += \
# Models
    $${PWD}/OAICreateServerPayload.h \
    $${PWD}/OAIDKIMRotationResponse.h \
    $${PWD}/OAIDomainCreationModel.h \
    $${PWD}/OAIDomainEditingModel.h \
    $${PWD}/OAIDomainExtendedInformation.h \
    $${PWD}/OAIDomainInformation.h \
    $${PWD}/OAIDomainListingResults.h \
    $${PWD}/OAIDomainSPFResult.h \
    $${PWD}/OAIEditServerPayload.h \
    $${PWD}/OAIExtendedServerInfo.h \
    $${PWD}/OAISenderListingResults.h \
    $${PWD}/OAISenderSignatureCreationModel.h \
    $${PWD}/OAISenderSignatureEditingModel.h \
    $${PWD}/OAISenderSignatureExtendedInformation.h \
    $${PWD}/OAISenderSignatureInformation.h \
    $${PWD}/OAIServerListingResponse.h \
    $${PWD}/OAIStandardPostmarkResponse.h \
    $${PWD}/OAITemplatesPushModel.h \
    $${PWD}/OAITemplatesPushResponse.h \
    $${PWD}/OAITemplatesPushResponse_Templates_inner.h \
# APIs
    $${PWD}/OAIDomainsAPIApi.h \
    $${PWD}/OAISenderSignaturesAPIApi.h \
    $${PWD}/OAIServerManagementAPIApi.h \
    $${PWD}/OAITemplatesAPIApi.h \
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
    $${PWD}/OAICreateServerPayload.cpp \
    $${PWD}/OAIDKIMRotationResponse.cpp \
    $${PWD}/OAIDomainCreationModel.cpp \
    $${PWD}/OAIDomainEditingModel.cpp \
    $${PWD}/OAIDomainExtendedInformation.cpp \
    $${PWD}/OAIDomainInformation.cpp \
    $${PWD}/OAIDomainListingResults.cpp \
    $${PWD}/OAIDomainSPFResult.cpp \
    $${PWD}/OAIEditServerPayload.cpp \
    $${PWD}/OAIExtendedServerInfo.cpp \
    $${PWD}/OAISenderListingResults.cpp \
    $${PWD}/OAISenderSignatureCreationModel.cpp \
    $${PWD}/OAISenderSignatureEditingModel.cpp \
    $${PWD}/OAISenderSignatureExtendedInformation.cpp \
    $${PWD}/OAISenderSignatureInformation.cpp \
    $${PWD}/OAIServerListingResponse.cpp \
    $${PWD}/OAIStandardPostmarkResponse.cpp \
    $${PWD}/OAITemplatesPushModel.cpp \
    $${PWD}/OAITemplatesPushResponse.cpp \
    $${PWD}/OAITemplatesPushResponse_Templates_inner.cpp \
# APIs
    $${PWD}/OAIDomainsAPIApi.cpp \
    $${PWD}/OAISenderSignaturesAPIApi.cpp \
    $${PWD}/OAIServerManagementAPIApi.cpp \
    $${PWD}/OAITemplatesAPIApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
