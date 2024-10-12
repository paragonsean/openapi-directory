QT += network

HEADERS += \
# Models
    $${PWD}/OAINotificationRecipientEmail_CreateOrUpdate_200_response.h \
    $${PWD}/OAINotificationRecipientEmail_ListByNotification_200_response.h \
    $${PWD}/OAINotificationRecipientEmail_ListByNotification_200_response_value_inner.h \
    $${PWD}/OAINotificationRecipientEmail_ListByNotification_200_response_value_inner_properties.h \
    $${PWD}/OAINotificationRecipientUser_CreateOrUpdate_200_response.h \
    $${PWD}/OAINotificationRecipientUser_ListByNotification_200_response.h \
    $${PWD}/OAINotificationRecipientUser_ListByNotification_200_response_value_inner.h \
    $${PWD}/OAINotificationRecipientUser_ListByNotification_200_response_value_inner_properties.h \
    $${PWD}/OAINotification_Get_200_response.h \
    $${PWD}/OAINotification_ListByService_200_response.h \
    $${PWD}/OAINotification_ListByService_200_response_value_inner.h \
    $${PWD}/OAINotification_ListByService_200_response_value_inner_properties.h \
    $${PWD}/OAINotification_ListByService_200_response_value_inner_properties_recipients.h \
    $${PWD}/OAINotification_ListByService_default_response.h \
    $${PWD}/OAINotification_ListByService_default_response_error.h \
    $${PWD}/OAINotification_ListByService_default_response_error_details_inner.h \
# APIs
    $${PWD}/OAINotificationApi.h \
    $${PWD}/OAINotificationRecipientEmailApi.h \
    $${PWD}/OAINotificationRecipientUserApi.h \
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
    $${PWD}/OAINotificationRecipientEmail_CreateOrUpdate_200_response.cpp \
    $${PWD}/OAINotificationRecipientEmail_ListByNotification_200_response.cpp \
    $${PWD}/OAINotificationRecipientEmail_ListByNotification_200_response_value_inner.cpp \
    $${PWD}/OAINotificationRecipientEmail_ListByNotification_200_response_value_inner_properties.cpp \
    $${PWD}/OAINotificationRecipientUser_CreateOrUpdate_200_response.cpp \
    $${PWD}/OAINotificationRecipientUser_ListByNotification_200_response.cpp \
    $${PWD}/OAINotificationRecipientUser_ListByNotification_200_response_value_inner.cpp \
    $${PWD}/OAINotificationRecipientUser_ListByNotification_200_response_value_inner_properties.cpp \
    $${PWD}/OAINotification_Get_200_response.cpp \
    $${PWD}/OAINotification_ListByService_200_response.cpp \
    $${PWD}/OAINotification_ListByService_200_response_value_inner.cpp \
    $${PWD}/OAINotification_ListByService_200_response_value_inner_properties.cpp \
    $${PWD}/OAINotification_ListByService_200_response_value_inner_properties_recipients.cpp \
    $${PWD}/OAINotification_ListByService_default_response.cpp \
    $${PWD}/OAINotification_ListByService_default_response_error.cpp \
    $${PWD}/OAINotification_ListByService_default_response_error_details_inner.cpp \
# APIs
    $${PWD}/OAINotificationApi.cpp \
    $${PWD}/OAINotificationRecipientEmailApi.cpp \
    $${PWD}/OAINotificationRecipientUserApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
