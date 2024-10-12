QT += network

HEADERS += \
# Models
    $${PWD}/OAIComplete_codename_lsit.h \
    $${PWD}/OAIComplete_codename_lsit_result_inner.h \
    $${PWD}/OAIDetailed_ordering_level_info.h \
    $${PWD}/OAIDetailed_ordering_level_info_result_inner.h \
    $${PWD}/OAIDetailed_ordering_level_info_result_inner_attributes_inner.h \
    $${PWD}/OAIDetailed_product_information.h \
    $${PWD}/OAIDetailed_product_information_result_inner.h \
    $${PWD}/OAIDetailed_product_information_result_inner_allOf_media_asset.h \
    $${PWD}/OAIDetailed_product_information_result_inner_allOf_reference_inner.h \
    $${PWD}/OAIDetailed_product_information_result_inner_allOf_tech_spec_inner.h \
    $${PWD}/OAIProduct_listing_level_info.h \
    $${PWD}/OAIProduct_listing_level_info_result_inner.h \
    $${PWD}/OAIProduct_listing_level_info_result_inner_highlights_info_inner.h \
    $${PWD}/OAIUnsuccessful_operation.h \
# APIs
    $${PWD}/OAIProductsApi.h \
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
    $${PWD}/OAIComplete_codename_lsit.cpp \
    $${PWD}/OAIComplete_codename_lsit_result_inner.cpp \
    $${PWD}/OAIDetailed_ordering_level_info.cpp \
    $${PWD}/OAIDetailed_ordering_level_info_result_inner.cpp \
    $${PWD}/OAIDetailed_ordering_level_info_result_inner_attributes_inner.cpp \
    $${PWD}/OAIDetailed_product_information.cpp \
    $${PWD}/OAIDetailed_product_information_result_inner.cpp \
    $${PWD}/OAIDetailed_product_information_result_inner_allOf_media_asset.cpp \
    $${PWD}/OAIDetailed_product_information_result_inner_allOf_reference_inner.cpp \
    $${PWD}/OAIDetailed_product_information_result_inner_allOf_tech_spec_inner.cpp \
    $${PWD}/OAIProduct_listing_level_info.cpp \
    $${PWD}/OAIProduct_listing_level_info_result_inner.cpp \
    $${PWD}/OAIProduct_listing_level_info_result_inner_highlights_info_inner.cpp \
    $${PWD}/OAIUnsuccessful_operation.cpp \
# APIs
    $${PWD}/OAIProductsApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
