# GoogleDocsApi.DocumentStyle

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**background** | [**Background**](Background.md) |  | [optional] 
**defaultFooterId** | **String** | The ID of the default footer. If not set, there&#39;s no default footer. This property is read-only. | [optional] 
**defaultHeaderId** | **String** | The ID of the default header. If not set, there&#39;s no default header. This property is read-only. | [optional] 
**evenPageFooterId** | **String** | The ID of the footer used only for even pages. The value of use_even_page_header_footer determines whether to use the default_footer_id or this value for the footer on even pages. If not set, there&#39;s no even page footer. This property is read-only. | [optional] 
**evenPageHeaderId** | **String** | The ID of the header used only for even pages. The value of use_even_page_header_footer determines whether to use the default_header_id or this value for the header on even pages. If not set, there&#39;s no even page header. This property is read-only. | [optional] 
**firstPageFooterId** | **String** | The ID of the footer used only for the first page. If not set then a unique footer for the first page does not exist. The value of use_first_page_header_footer determines whether to use the default_footer_id or this value for the footer on the first page. If not set, there&#39;s no first page footer. This property is read-only. | [optional] 
**firstPageHeaderId** | **String** | The ID of the header used only for the first page. If not set then a unique header for the first page does not exist. The value of use_first_page_header_footer determines whether to use the default_header_id or this value for the header on the first page. If not set, there&#39;s no first page header. This property is read-only. | [optional] 
**flipPageOrientation** | **Boolean** | Optional. Indicates whether to flip the dimensions of the page_size, which allows changing the page orientation between portrait and landscape. | [optional] 
**marginBottom** | [**Dimension**](Dimension.md) |  | [optional] 
**marginFooter** | [**Dimension**](Dimension.md) |  | [optional] 
**marginHeader** | [**Dimension**](Dimension.md) |  | [optional] 
**marginLeft** | [**Dimension**](Dimension.md) |  | [optional] 
**marginRight** | [**Dimension**](Dimension.md) |  | [optional] 
**marginTop** | [**Dimension**](Dimension.md) |  | [optional] 
**pageNumberStart** | **Number** | The page number from which to start counting the number of pages. | [optional] 
**pageSize** | [**Size**](Size.md) |  | [optional] 
**useCustomHeaderFooterMargins** | **Boolean** | Indicates whether DocumentStyle margin_header, SectionStyle margin_header and DocumentStyle margin_footer, SectionStyle margin_footer are respected. When false, the default values in the Docs editor for header and footer margin are used. This property is read-only. | [optional] 
**useEvenPageHeaderFooter** | **Boolean** | Indicates whether to use the even page header / footer IDs for the even pages. | [optional] 
**useFirstPageHeaderFooter** | **Boolean** | Indicates whether to use the first page header / footer IDs for the first page. | [optional] 


