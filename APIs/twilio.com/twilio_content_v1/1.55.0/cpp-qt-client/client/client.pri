QT += network

HEADERS += \
# Models
    $${PWD}/OAIContent_v1_content.h \
    $${PWD}/OAIContent_v1_content_and_approvals.h \
    $${PWD}/OAIContent_v1_content_approval_fetch.h \
    $${PWD}/OAIContent_v1_legacy_content.h \
    $${PWD}/OAIListContentAndApprovalsResponse.h \
    $${PWD}/OAIListContentResponse.h \
    $${PWD}/OAIListContentResponse_meta.h \
    $${PWD}/OAIListLegacyContentResponse.h \
# APIs
    $${PWD}/OAIContentV1ApprovalFetchApi.h \
    $${PWD}/OAIContentV1ContentApi.h \
    $${PWD}/OAIContentV1ContentAndApprovalsApi.h \
    $${PWD}/OAIContentV1LegacyContentApi.h \
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
    $${PWD}/OAIContent_v1_content.cpp \
    $${PWD}/OAIContent_v1_content_and_approvals.cpp \
    $${PWD}/OAIContent_v1_content_approval_fetch.cpp \
    $${PWD}/OAIContent_v1_legacy_content.cpp \
    $${PWD}/OAIListContentAndApprovalsResponse.cpp \
    $${PWD}/OAIListContentResponse.cpp \
    $${PWD}/OAIListContentResponse_meta.cpp \
    $${PWD}/OAIListLegacyContentResponse.cpp \
# APIs
    $${PWD}/OAIContentV1ApprovalFetchApi.cpp \
    $${PWD}/OAIContentV1ContentApi.cpp \
    $${PWD}/OAIContentV1ContentAndApprovalsApi.cpp \
    $${PWD}/OAIContentV1LegacyContentApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
