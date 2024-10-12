QT += network

HEADERS += \
# Models
    $${PWD}/OAICreateContactInMailingList.h \
    $${PWD}/OAICreateDistributionLinks.h \
    $${PWD}/OAIDistributionsResponse.h \
    $${PWD}/OAIDistributionsResponse_meta.h \
    $${PWD}/OAIDistributionsResponse_result.h \
    $${PWD}/OAIDistributionsResponse_result_elements_inner.h \
    $${PWD}/OAIDistributionsResponse_result_elements_inner_headers.h \
    $${PWD}/OAIDistributionsResponse_result_elements_inner_message.h \
    $${PWD}/OAIDistributionsResponse_result_elements_inner_recipients.h \
    $${PWD}/OAIDistributionsResponse_result_elements_inner_stats.h \
    $${PWD}/OAIDistributionsResponse_result_elements_inner_surveyLink.h \
    $${PWD}/OAIEventSubscriptionHookSchema.h \
    $${PWD}/OAIEventSubscriptionHookSchema__formdata_inner.h \
    $${PWD}/OAIEventSubscriptionsResponse.h \
    $${PWD}/OAIEventSubscriptionsResponse_result.h \
    $${PWD}/OAIEventSubscriptionsResponse_result_meta.h \
    $${PWD}/OAIEventSubscriptionsResponse_result_result.h \
    $${PWD}/OAIRetrieveDistributionLinksResponse.h \
    $${PWD}/OAIRetrieveDistributionLinksResponse_result.h \
    $${PWD}/OAIRetrieveDistributionLinksResponse_result_elements_inner.h \
    $${PWD}/OAISubscribeToEventBody.h \
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
    $${PWD}/OAICreateContactInMailingList.cpp \
    $${PWD}/OAICreateDistributionLinks.cpp \
    $${PWD}/OAIDistributionsResponse.cpp \
    $${PWD}/OAIDistributionsResponse_meta.cpp \
    $${PWD}/OAIDistributionsResponse_result.cpp \
    $${PWD}/OAIDistributionsResponse_result_elements_inner.cpp \
    $${PWD}/OAIDistributionsResponse_result_elements_inner_headers.cpp \
    $${PWD}/OAIDistributionsResponse_result_elements_inner_message.cpp \
    $${PWD}/OAIDistributionsResponse_result_elements_inner_recipients.cpp \
    $${PWD}/OAIDistributionsResponse_result_elements_inner_stats.cpp \
    $${PWD}/OAIDistributionsResponse_result_elements_inner_surveyLink.cpp \
    $${PWD}/OAIEventSubscriptionHookSchema.cpp \
    $${PWD}/OAIEventSubscriptionHookSchema__formdata_inner.cpp \
    $${PWD}/OAIEventSubscriptionsResponse.cpp \
    $${PWD}/OAIEventSubscriptionsResponse_result.cpp \
    $${PWD}/OAIEventSubscriptionsResponse_result_meta.cpp \
    $${PWD}/OAIEventSubscriptionsResponse_result_result.cpp \
    $${PWD}/OAIRetrieveDistributionLinksResponse.cpp \
    $${PWD}/OAIRetrieveDistributionLinksResponse_result.cpp \
    $${PWD}/OAIRetrieveDistributionLinksResponse_result_elements_inner.cpp \
    $${PWD}/OAISubscribeToEventBody.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
