QT += network

HEADERS += \
# Models
    $${PWD}/OAIAcceptSellerLeadRequest.h \
    $${PWD}/OAIAccountable.h \
    $${PWD}/OAIAddress.h \
    $${PWD}/OAIAvailableSalesChannel.h \
    $${PWD}/OAIBulkUpsertSellerCommissionsRequest.h \
    $${PWD}/OAICreateSellerLeadRequest.h \
    $${PWD}/OAIGetMatchedOffersResponse.h \
    $${PWD}/OAIGroups.h \
    $${PWD}/OAIMainImage.h \
    $${PWD}/OAIOffer.h \
    $${PWD}/OAIOffersPerSalesChannel.h \
    $${PWD}/OAIRequest_body_inner.h \
    $${PWD}/OAIResendSellerLeadRequestRequest.h \
    $${PWD}/OAISellerCommissionConfiguration.h \
    $${PWD}/OAISku2.h \
    $${PWD}/OAIUpsertMappingRequest.h \
    $${PWD}/OAIUpsertSellerCommissionsRequest.h \
    $${PWD}/OAIUpsertSellerRequest.h \
# APIs
    $${PWD}/OAIMatchedOffersApi.h \
    $${PWD}/OAINotificationApi.h \
    $${PWD}/OAISalesChannelMappingApi.h \
    $${PWD}/OAISellerCommissionsApi.h \
    $${PWD}/OAISellerInviteApi.h \
    $${PWD}/OAISellersApi.h \
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
    $${PWD}/OAIAcceptSellerLeadRequest.cpp \
    $${PWD}/OAIAccountable.cpp \
    $${PWD}/OAIAddress.cpp \
    $${PWD}/OAIAvailableSalesChannel.cpp \
    $${PWD}/OAIBulkUpsertSellerCommissionsRequest.cpp \
    $${PWD}/OAICreateSellerLeadRequest.cpp \
    $${PWD}/OAIGetMatchedOffersResponse.cpp \
    $${PWD}/OAIGroups.cpp \
    $${PWD}/OAIMainImage.cpp \
    $${PWD}/OAIOffer.cpp \
    $${PWD}/OAIOffersPerSalesChannel.cpp \
    $${PWD}/OAIRequest_body_inner.cpp \
    $${PWD}/OAIResendSellerLeadRequestRequest.cpp \
    $${PWD}/OAISellerCommissionConfiguration.cpp \
    $${PWD}/OAISku2.cpp \
    $${PWD}/OAIUpsertMappingRequest.cpp \
    $${PWD}/OAIUpsertSellerCommissionsRequest.cpp \
    $${PWD}/OAIUpsertSellerRequest.cpp \
# APIs
    $${PWD}/OAIMatchedOffersApi.cpp \
    $${PWD}/OAINotificationApi.cpp \
    $${PWD}/OAISalesChannelMappingApi.cpp \
    $${PWD}/OAISellerCommissionsApi.cpp \
    $${PWD}/OAISellerInviteApi.cpp \
    $${PWD}/OAISellersApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
