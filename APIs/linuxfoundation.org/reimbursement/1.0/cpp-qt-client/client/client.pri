QT += network

HEADERS += \
# Models
    $${PWD}/OAIContact.h \
    $${PWD}/OAICreateReimbursement_request.h \
    $${PWD}/OAIError_response.h \
    $${PWD}/OAIHealth.h \
    $${PWD}/OAIHealth_status.h \
    $${PWD}/OAIPolicy_create_input.h \
    $${PWD}/OAIPolicy_reset_input.h \
    $${PWD}/OAIPolicy_tag_input.h \
    $${PWD}/OAIPolicy_update_input.h \
# APIs
    $${PWD}/OAIDefaultApi.h \
    $${PWD}/OAIDocsApi.h \
    $${PWD}/OAIReimbursementApi.h \
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
    $${PWD}/OAIContact.cpp \
    $${PWD}/OAICreateReimbursement_request.cpp \
    $${PWD}/OAIError_response.cpp \
    $${PWD}/OAIHealth.cpp \
    $${PWD}/OAIHealth_status.cpp \
    $${PWD}/OAIPolicy_create_input.cpp \
    $${PWD}/OAIPolicy_reset_input.cpp \
    $${PWD}/OAIPolicy_tag_input.cpp \
    $${PWD}/OAIPolicy_update_input.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
    $${PWD}/OAIDocsApi.cpp \
    $${PWD}/OAIReimbursementApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
