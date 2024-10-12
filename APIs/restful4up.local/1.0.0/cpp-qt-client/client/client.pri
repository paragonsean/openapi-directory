QT += network

HEADERS += \
# Models
    $${PWD}/OAIApplyYaraRules_200_response.h \
    $${PWD}/OAIApply_yara_rule.h \
    $${PWD}/OAIApply_yara_rule_matched_yara_rules_inner_inner.h \
    $${PWD}/OAIEmulationOutput_200_response.h \
    $${PWD}/OAIError.h \
    $${PWD}/OAIGeneratePartialYaraRule_200_response.h \
    $${PWD}/OAIYara.h \
    $${PWD}/OAIYara_meta.h \
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
    $${PWD}/OAIApplyYaraRules_200_response.cpp \
    $${PWD}/OAIApply_yara_rule.cpp \
    $${PWD}/OAIApply_yara_rule_matched_yara_rules_inner_inner.cpp \
    $${PWD}/OAIEmulationOutput_200_response.cpp \
    $${PWD}/OAIError.cpp \
    $${PWD}/OAIGeneratePartialYaraRule_200_response.cpp \
    $${PWD}/OAIYara.cpp \
    $${PWD}/OAIYara_meta.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
