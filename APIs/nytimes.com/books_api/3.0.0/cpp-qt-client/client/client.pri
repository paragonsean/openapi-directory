QT += network

HEADERS += \
# Models
    $${PWD}/OAIGET_lists_best_sellers_history_json_200_response.h \
    $${PWD}/OAIGET_lists_best_sellers_history_json_200_response_results_inner.h \
    $${PWD}/OAIGET_lists_best_sellers_history_json_200_response_results_inner_ranks_history_inner.h \
    $${PWD}/OAIGET_lists_date_list_json_200_response.h \
    $${PWD}/OAIGET_lists_date_list_json_200_response_results.h \
    $${PWD}/OAIGET_lists_date_list_json_200_response_results_books_inner.h \
    $${PWD}/OAIGET_lists_format_200_response.h \
    $${PWD}/OAIGET_lists_format_200_response_results_inner.h \
    $${PWD}/OAIGET_lists_format_200_response_results_inner_book_details_inner.h \
    $${PWD}/OAIGET_lists_format_200_response_results_inner_isbns_inner.h \
    $${PWD}/OAIGET_lists_format_200_response_results_inner_reviews_inner.h \
    $${PWD}/OAIGET_lists_names_format_200_response.h \
    $${PWD}/OAIGET_lists_names_format_200_response_results_inner.h \
    $${PWD}/OAIGET_lists_overview_format_200_response.h \
    $${PWD}/OAIGET_lists_overview_format_200_response_results.h \
    $${PWD}/OAIGET_lists_overview_format_200_response_results_lists_inner.h \
    $${PWD}/OAIGET_lists_overview_format_200_response_results_lists_inner_books_inner.h \
    $${PWD}/OAIGET_reviews_format_200_response.h \
    $${PWD}/OAIGET_reviews_format_200_response_results_inner.h \
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
    $${PWD}/OAIGET_lists_best_sellers_history_json_200_response.cpp \
    $${PWD}/OAIGET_lists_best_sellers_history_json_200_response_results_inner.cpp \
    $${PWD}/OAIGET_lists_best_sellers_history_json_200_response_results_inner_ranks_history_inner.cpp \
    $${PWD}/OAIGET_lists_date_list_json_200_response.cpp \
    $${PWD}/OAIGET_lists_date_list_json_200_response_results.cpp \
    $${PWD}/OAIGET_lists_date_list_json_200_response_results_books_inner.cpp \
    $${PWD}/OAIGET_lists_format_200_response.cpp \
    $${PWD}/OAIGET_lists_format_200_response_results_inner.cpp \
    $${PWD}/OAIGET_lists_format_200_response_results_inner_book_details_inner.cpp \
    $${PWD}/OAIGET_lists_format_200_response_results_inner_isbns_inner.cpp \
    $${PWD}/OAIGET_lists_format_200_response_results_inner_reviews_inner.cpp \
    $${PWD}/OAIGET_lists_names_format_200_response.cpp \
    $${PWD}/OAIGET_lists_names_format_200_response_results_inner.cpp \
    $${PWD}/OAIGET_lists_overview_format_200_response.cpp \
    $${PWD}/OAIGET_lists_overview_format_200_response_results.cpp \
    $${PWD}/OAIGET_lists_overview_format_200_response_results_lists_inner.cpp \
    $${PWD}/OAIGET_lists_overview_format_200_response_results_lists_inner_books_inner.cpp \
    $${PWD}/OAIGET_reviews_format_200_response.cpp \
    $${PWD}/OAIGET_reviews_format_200_response_results_inner.cpp \
# APIs
    $${PWD}/OAIDefaultApi.cpp \
# Others
    $${PWD}/OAIHelpers.cpp \
    $${PWD}/OAIHttpRequest.cpp \
    $${PWD}/OAIHttpFileElement.cpp \
    $${PWD}/OAIOauth.cpp
