QT += network

HEADERS += \
# Models
    $${PWD}/OAIBinding_enum_binding_type.h \
    $${PWD}/OAICredential_enum_push_service.h \
    $${PWD}/OAIListBindingResponse.h \
    $${PWD}/OAIListCredentialResponse.h \
    $${PWD}/OAIListCredentialResponse_meta.h \
    $${PWD}/OAIListServiceResponse.h \
    $${PWD}/OAINotification_enum_priority.h \
    $${PWD}/OAINotify_v1_credential.h \
    $${PWD}/OAINotify_v1_service.h \
    $${PWD}/OAINotify_v1_service_binding.h \
    $${PWD}/OAINotify_v1_service_notification.h \
# APIs
    $${PWD}/OAINotifyV1BindingApi.h \
    $${PWD}/OAINotifyV1CredentialApi.h \
    $${PWD}/OAINotifyV1NotificationApi.h \
    $${PWD}/OAINotifyV1ServiceApi.h \
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
    $${PWD}/OAIBinding_enum_binding_type.cpp \
    $${PWD}/OAICredential_enum_push_service.cpp \
    $${PWD}/OAIListBindingResponse.cpp \
    $${PWD}/OAIListCredentialResponse.cpp \
    $${PWD}/OAIListCredentialResponse_meta.cpp \
    $${PWD}/OAIListServiceResponse.cpp \
    $${PWD}/OAINotification_enum_priority.cpp \
    $${PWD}/OAINotify_v1_credential.cpp \
    $${PWD}/OAINotify_v1_service.cpp \
    $${PWD}/OAINotify_v1_service_binding.cpp \
    $${PWD}/OAINotify_v1_service_notification.cpp \
# APIs
    $${PWD}/OAINotifyV1BindingApi.cpp \
    $${PWD}/OAINotifyV1CredentialApi.cpp \
    $${PWD}/OAINotifyV1NotificationApi.cpp \
    $${PWD}/OAINotifyV1ServiceApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
