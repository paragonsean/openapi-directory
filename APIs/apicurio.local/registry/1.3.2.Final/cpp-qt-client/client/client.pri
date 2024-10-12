QT += network

HEADERS += \
# Models
    $${PWD}/OAIArtifactMetaData.h \
    $${PWD}/OAIArtifactSearchResults.h \
    $${PWD}/OAIArtifactState.h \
    $${PWD}/OAIArtifactType.h \
    $${PWD}/OAIEditableMetaData.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIRule.h \
    $${PWD}/OAIRuleType.h \
    $${PWD}/OAISearchOver.h \
    $${PWD}/OAISearchedArtifact.h \
    $${PWD}/OAISearchedVersion.h \
    $${PWD}/OAISortOrder.h \
    $${PWD}/OAIUpdateState.h \
    $${PWD}/OAIVersionMetaData.h \
    $${PWD}/OAIVersionSearchResults.h \
# APIs
    $${PWD}/OAIArtifactRulesApi.h \
    $${PWD}/OAIArtifactsApi.h \
    $${PWD}/OAIGlobalRulesApi.h \
    $${PWD}/OAIMetadataApi.h \
    $${PWD}/OAISearchApi.h \
    $${PWD}/OAIVersionsApi.h \
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
    $${PWD}/OAIArtifactMetaData.cpp \
    $${PWD}/OAIArtifactSearchResults.cpp \
    $${PWD}/OAIArtifactState.cpp \
    $${PWD}/OAIArtifactType.cpp \
    $${PWD}/OAIEditableMetaData.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIRule.cpp \
    $${PWD}/OAIRuleType.cpp \
    $${PWD}/OAISearchOver.cpp \
    $${PWD}/OAISearchedArtifact.cpp \
    $${PWD}/OAISearchedVersion.cpp \
    $${PWD}/OAISortOrder.cpp \
    $${PWD}/OAIUpdateState.cpp \
    $${PWD}/OAIVersionMetaData.cpp \
    $${PWD}/OAIVersionSearchResults.cpp \
# APIs
    $${PWD}/OAIArtifactRulesApi.cpp \
    $${PWD}/OAIArtifactsApi.cpp \
    $${PWD}/OAIGlobalRulesApi.cpp \
    $${PWD}/OAIMetadataApi.cpp \
    $${PWD}/OAISearchApi.cpp \
    $${PWD}/OAIVersionsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
