# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.add_banding_request import AddBandingRequest
from openapi_server.models.add_chart_request import AddChartRequest
from openapi_server.models.add_conditional_format_rule_request import AddConditionalFormatRuleRequest
from openapi_server.models.add_data_source_request import AddDataSourceRequest
from openapi_server.models.add_dimension_group_request import AddDimensionGroupRequest
from openapi_server.models.add_filter_view_request import AddFilterViewRequest
from openapi_server.models.add_named_range_request import AddNamedRangeRequest
from openapi_server.models.add_protected_range_request import AddProtectedRangeRequest
from openapi_server.models.add_sheet_request import AddSheetRequest
from openapi_server.models.add_slicer_request import AddSlicerRequest
from openapi_server.models.append_cells_request import AppendCellsRequest
from openapi_server.models.append_dimension_request import AppendDimensionRequest
from openapi_server.models.auto_fill_request import AutoFillRequest
from openapi_server.models.auto_resize_dimensions_request import AutoResizeDimensionsRequest
from openapi_server.models.clear_basic_filter_request import ClearBasicFilterRequest
from openapi_server.models.copy_paste_request import CopyPasteRequest
from openapi_server.models.create_developer_metadata_request import CreateDeveloperMetadataRequest
from openapi_server.models.cut_paste_request import CutPasteRequest
from openapi_server.models.delete_banding_request import DeleteBandingRequest
from openapi_server.models.delete_conditional_format_rule_request import DeleteConditionalFormatRuleRequest
from openapi_server.models.delete_data_source_request import DeleteDataSourceRequest
from openapi_server.models.delete_developer_metadata_request import DeleteDeveloperMetadataRequest
from openapi_server.models.delete_dimension_group_request import DeleteDimensionGroupRequest
from openapi_server.models.delete_dimension_request import DeleteDimensionRequest
from openapi_server.models.delete_duplicates_request import DeleteDuplicatesRequest
from openapi_server.models.delete_embedded_object_request import DeleteEmbeddedObjectRequest
from openapi_server.models.delete_filter_view_request import DeleteFilterViewRequest
from openapi_server.models.delete_named_range_request import DeleteNamedRangeRequest
from openapi_server.models.delete_protected_range_request import DeleteProtectedRangeRequest
from openapi_server.models.delete_range_request import DeleteRangeRequest
from openapi_server.models.delete_sheet_request import DeleteSheetRequest
from openapi_server.models.duplicate_filter_view_request import DuplicateFilterViewRequest
from openapi_server.models.duplicate_sheet_request import DuplicateSheetRequest
from openapi_server.models.find_replace_request import FindReplaceRequest
from openapi_server.models.insert_dimension_request import InsertDimensionRequest
from openapi_server.models.insert_range_request import InsertRangeRequest
from openapi_server.models.merge_cells_request import MergeCellsRequest
from openapi_server.models.move_dimension_request import MoveDimensionRequest
from openapi_server.models.paste_data_request import PasteDataRequest
from openapi_server.models.randomize_range_request import RandomizeRangeRequest
from openapi_server.models.refresh_data_source_request import RefreshDataSourceRequest
from openapi_server.models.repeat_cell_request import RepeatCellRequest
from openapi_server.models.set_basic_filter_request import SetBasicFilterRequest
from openapi_server.models.set_data_validation_request import SetDataValidationRequest
from openapi_server.models.sort_range_request import SortRangeRequest
from openapi_server.models.text_to_columns_request import TextToColumnsRequest
from openapi_server.models.trim_whitespace_request import TrimWhitespaceRequest
from openapi_server.models.unmerge_cells_request import UnmergeCellsRequest
from openapi_server.models.update_banding_request import UpdateBandingRequest
from openapi_server.models.update_borders_request import UpdateBordersRequest
from openapi_server.models.update_cells_request import UpdateCellsRequest
from openapi_server.models.update_chart_spec_request import UpdateChartSpecRequest
from openapi_server.models.update_conditional_format_rule_request import UpdateConditionalFormatRuleRequest
from openapi_server.models.update_data_source_request import UpdateDataSourceRequest
from openapi_server.models.update_developer_metadata_request import UpdateDeveloperMetadataRequest
from openapi_server.models.update_dimension_group_request import UpdateDimensionGroupRequest
from openapi_server.models.update_dimension_properties_request import UpdateDimensionPropertiesRequest
from openapi_server.models.update_embedded_object_border_request import UpdateEmbeddedObjectBorderRequest
from openapi_server.models.update_embedded_object_position_request import UpdateEmbeddedObjectPositionRequest
from openapi_server.models.update_filter_view_request import UpdateFilterViewRequest
from openapi_server.models.update_named_range_request import UpdateNamedRangeRequest
from openapi_server.models.update_protected_range_request import UpdateProtectedRangeRequest
from openapi_server.models.update_sheet_properties_request import UpdateSheetPropertiesRequest
from openapi_server.models.update_slicer_spec_request import UpdateSlicerSpecRequest
from openapi_server.models.update_spreadsheet_properties_request import UpdateSpreadsheetPropertiesRequest
from openapi_server import util


class Request(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, add_banding: AddBandingRequest=None, add_chart: AddChartRequest=None, add_conditional_format_rule: AddConditionalFormatRuleRequest=None, add_data_source: AddDataSourceRequest=None, add_dimension_group: AddDimensionGroupRequest=None, add_filter_view: AddFilterViewRequest=None, add_named_range: AddNamedRangeRequest=None, add_protected_range: AddProtectedRangeRequest=None, add_sheet: AddSheetRequest=None, add_slicer: AddSlicerRequest=None, append_cells: AppendCellsRequest=None, append_dimension: AppendDimensionRequest=None, auto_fill: AutoFillRequest=None, auto_resize_dimensions: AutoResizeDimensionsRequest=None, clear_basic_filter: ClearBasicFilterRequest=None, copy_paste: CopyPasteRequest=None, create_developer_metadata: CreateDeveloperMetadataRequest=None, cut_paste: CutPasteRequest=None, delete_banding: DeleteBandingRequest=None, delete_conditional_format_rule: DeleteConditionalFormatRuleRequest=None, delete_data_source: DeleteDataSourceRequest=None, delete_developer_metadata: DeleteDeveloperMetadataRequest=None, delete_dimension: DeleteDimensionRequest=None, delete_dimension_group: DeleteDimensionGroupRequest=None, delete_duplicates: DeleteDuplicatesRequest=None, delete_embedded_object: DeleteEmbeddedObjectRequest=None, delete_filter_view: DeleteFilterViewRequest=None, delete_named_range: DeleteNamedRangeRequest=None, delete_protected_range: DeleteProtectedRangeRequest=None, delete_range: DeleteRangeRequest=None, delete_sheet: DeleteSheetRequest=None, duplicate_filter_view: DuplicateFilterViewRequest=None, duplicate_sheet: DuplicateSheetRequest=None, find_replace: FindReplaceRequest=None, insert_dimension: InsertDimensionRequest=None, insert_range: InsertRangeRequest=None, merge_cells: MergeCellsRequest=None, move_dimension: MoveDimensionRequest=None, paste_data: PasteDataRequest=None, randomize_range: RandomizeRangeRequest=None, refresh_data_source: RefreshDataSourceRequest=None, repeat_cell: RepeatCellRequest=None, set_basic_filter: SetBasicFilterRequest=None, set_data_validation: SetDataValidationRequest=None, sort_range: SortRangeRequest=None, text_to_columns: TextToColumnsRequest=None, trim_whitespace: TrimWhitespaceRequest=None, unmerge_cells: UnmergeCellsRequest=None, update_banding: UpdateBandingRequest=None, update_borders: UpdateBordersRequest=None, update_cells: UpdateCellsRequest=None, update_chart_spec: UpdateChartSpecRequest=None, update_conditional_format_rule: UpdateConditionalFormatRuleRequest=None, update_data_source: UpdateDataSourceRequest=None, update_developer_metadata: UpdateDeveloperMetadataRequest=None, update_dimension_group: UpdateDimensionGroupRequest=None, update_dimension_properties: UpdateDimensionPropertiesRequest=None, update_embedded_object_border: UpdateEmbeddedObjectBorderRequest=None, update_embedded_object_position: UpdateEmbeddedObjectPositionRequest=None, update_filter_view: UpdateFilterViewRequest=None, update_named_range: UpdateNamedRangeRequest=None, update_protected_range: UpdateProtectedRangeRequest=None, update_sheet_properties: UpdateSheetPropertiesRequest=None, update_slicer_spec: UpdateSlicerSpecRequest=None, update_spreadsheet_properties: UpdateSpreadsheetPropertiesRequest=None):
        """Request - a model defined in OpenAPI

        :param add_banding: The add_banding of this Request.
        :param add_chart: The add_chart of this Request.
        :param add_conditional_format_rule: The add_conditional_format_rule of this Request.
        :param add_data_source: The add_data_source of this Request.
        :param add_dimension_group: The add_dimension_group of this Request.
        :param add_filter_view: The add_filter_view of this Request.
        :param add_named_range: The add_named_range of this Request.
        :param add_protected_range: The add_protected_range of this Request.
        :param add_sheet: The add_sheet of this Request.
        :param add_slicer: The add_slicer of this Request.
        :param append_cells: The append_cells of this Request.
        :param append_dimension: The append_dimension of this Request.
        :param auto_fill: The auto_fill of this Request.
        :param auto_resize_dimensions: The auto_resize_dimensions of this Request.
        :param clear_basic_filter: The clear_basic_filter of this Request.
        :param copy_paste: The copy_paste of this Request.
        :param create_developer_metadata: The create_developer_metadata of this Request.
        :param cut_paste: The cut_paste of this Request.
        :param delete_banding: The delete_banding of this Request.
        :param delete_conditional_format_rule: The delete_conditional_format_rule of this Request.
        :param delete_data_source: The delete_data_source of this Request.
        :param delete_developer_metadata: The delete_developer_metadata of this Request.
        :param delete_dimension: The delete_dimension of this Request.
        :param delete_dimension_group: The delete_dimension_group of this Request.
        :param delete_duplicates: The delete_duplicates of this Request.
        :param delete_embedded_object: The delete_embedded_object of this Request.
        :param delete_filter_view: The delete_filter_view of this Request.
        :param delete_named_range: The delete_named_range of this Request.
        :param delete_protected_range: The delete_protected_range of this Request.
        :param delete_range: The delete_range of this Request.
        :param delete_sheet: The delete_sheet of this Request.
        :param duplicate_filter_view: The duplicate_filter_view of this Request.
        :param duplicate_sheet: The duplicate_sheet of this Request.
        :param find_replace: The find_replace of this Request.
        :param insert_dimension: The insert_dimension of this Request.
        :param insert_range: The insert_range of this Request.
        :param merge_cells: The merge_cells of this Request.
        :param move_dimension: The move_dimension of this Request.
        :param paste_data: The paste_data of this Request.
        :param randomize_range: The randomize_range of this Request.
        :param refresh_data_source: The refresh_data_source of this Request.
        :param repeat_cell: The repeat_cell of this Request.
        :param set_basic_filter: The set_basic_filter of this Request.
        :param set_data_validation: The set_data_validation of this Request.
        :param sort_range: The sort_range of this Request.
        :param text_to_columns: The text_to_columns of this Request.
        :param trim_whitespace: The trim_whitespace of this Request.
        :param unmerge_cells: The unmerge_cells of this Request.
        :param update_banding: The update_banding of this Request.
        :param update_borders: The update_borders of this Request.
        :param update_cells: The update_cells of this Request.
        :param update_chart_spec: The update_chart_spec of this Request.
        :param update_conditional_format_rule: The update_conditional_format_rule of this Request.
        :param update_data_source: The update_data_source of this Request.
        :param update_developer_metadata: The update_developer_metadata of this Request.
        :param update_dimension_group: The update_dimension_group of this Request.
        :param update_dimension_properties: The update_dimension_properties of this Request.
        :param update_embedded_object_border: The update_embedded_object_border of this Request.
        :param update_embedded_object_position: The update_embedded_object_position of this Request.
        :param update_filter_view: The update_filter_view of this Request.
        :param update_named_range: The update_named_range of this Request.
        :param update_protected_range: The update_protected_range of this Request.
        :param update_sheet_properties: The update_sheet_properties of this Request.
        :param update_slicer_spec: The update_slicer_spec of this Request.
        :param update_spreadsheet_properties: The update_spreadsheet_properties of this Request.
        """
        self.openapi_types = {
            'add_banding': AddBandingRequest,
            'add_chart': AddChartRequest,
            'add_conditional_format_rule': AddConditionalFormatRuleRequest,
            'add_data_source': AddDataSourceRequest,
            'add_dimension_group': AddDimensionGroupRequest,
            'add_filter_view': AddFilterViewRequest,
            'add_named_range': AddNamedRangeRequest,
            'add_protected_range': AddProtectedRangeRequest,
            'add_sheet': AddSheetRequest,
            'add_slicer': AddSlicerRequest,
            'append_cells': AppendCellsRequest,
            'append_dimension': AppendDimensionRequest,
            'auto_fill': AutoFillRequest,
            'auto_resize_dimensions': AutoResizeDimensionsRequest,
            'clear_basic_filter': ClearBasicFilterRequest,
            'copy_paste': CopyPasteRequest,
            'create_developer_metadata': CreateDeveloperMetadataRequest,
            'cut_paste': CutPasteRequest,
            'delete_banding': DeleteBandingRequest,
            'delete_conditional_format_rule': DeleteConditionalFormatRuleRequest,
            'delete_data_source': DeleteDataSourceRequest,
            'delete_developer_metadata': DeleteDeveloperMetadataRequest,
            'delete_dimension': DeleteDimensionRequest,
            'delete_dimension_group': DeleteDimensionGroupRequest,
            'delete_duplicates': DeleteDuplicatesRequest,
            'delete_embedded_object': DeleteEmbeddedObjectRequest,
            'delete_filter_view': DeleteFilterViewRequest,
            'delete_named_range': DeleteNamedRangeRequest,
            'delete_protected_range': DeleteProtectedRangeRequest,
            'delete_range': DeleteRangeRequest,
            'delete_sheet': DeleteSheetRequest,
            'duplicate_filter_view': DuplicateFilterViewRequest,
            'duplicate_sheet': DuplicateSheetRequest,
            'find_replace': FindReplaceRequest,
            'insert_dimension': InsertDimensionRequest,
            'insert_range': InsertRangeRequest,
            'merge_cells': MergeCellsRequest,
            'move_dimension': MoveDimensionRequest,
            'paste_data': PasteDataRequest,
            'randomize_range': RandomizeRangeRequest,
            'refresh_data_source': RefreshDataSourceRequest,
            'repeat_cell': RepeatCellRequest,
            'set_basic_filter': SetBasicFilterRequest,
            'set_data_validation': SetDataValidationRequest,
            'sort_range': SortRangeRequest,
            'text_to_columns': TextToColumnsRequest,
            'trim_whitespace': TrimWhitespaceRequest,
            'unmerge_cells': UnmergeCellsRequest,
            'update_banding': UpdateBandingRequest,
            'update_borders': UpdateBordersRequest,
            'update_cells': UpdateCellsRequest,
            'update_chart_spec': UpdateChartSpecRequest,
            'update_conditional_format_rule': UpdateConditionalFormatRuleRequest,
            'update_data_source': UpdateDataSourceRequest,
            'update_developer_metadata': UpdateDeveloperMetadataRequest,
            'update_dimension_group': UpdateDimensionGroupRequest,
            'update_dimension_properties': UpdateDimensionPropertiesRequest,
            'update_embedded_object_border': UpdateEmbeddedObjectBorderRequest,
            'update_embedded_object_position': UpdateEmbeddedObjectPositionRequest,
            'update_filter_view': UpdateFilterViewRequest,
            'update_named_range': UpdateNamedRangeRequest,
            'update_protected_range': UpdateProtectedRangeRequest,
            'update_sheet_properties': UpdateSheetPropertiesRequest,
            'update_slicer_spec': UpdateSlicerSpecRequest,
            'update_spreadsheet_properties': UpdateSpreadsheetPropertiesRequest
        }

        self.attribute_map = {
            'add_banding': 'addBanding',
            'add_chart': 'addChart',
            'add_conditional_format_rule': 'addConditionalFormatRule',
            'add_data_source': 'addDataSource',
            'add_dimension_group': 'addDimensionGroup',
            'add_filter_view': 'addFilterView',
            'add_named_range': 'addNamedRange',
            'add_protected_range': 'addProtectedRange',
            'add_sheet': 'addSheet',
            'add_slicer': 'addSlicer',
            'append_cells': 'appendCells',
            'append_dimension': 'appendDimension',
            'auto_fill': 'autoFill',
            'auto_resize_dimensions': 'autoResizeDimensions',
            'clear_basic_filter': 'clearBasicFilter',
            'copy_paste': 'copyPaste',
            'create_developer_metadata': 'createDeveloperMetadata',
            'cut_paste': 'cutPaste',
            'delete_banding': 'deleteBanding',
            'delete_conditional_format_rule': 'deleteConditionalFormatRule',
            'delete_data_source': 'deleteDataSource',
            'delete_developer_metadata': 'deleteDeveloperMetadata',
            'delete_dimension': 'deleteDimension',
            'delete_dimension_group': 'deleteDimensionGroup',
            'delete_duplicates': 'deleteDuplicates',
            'delete_embedded_object': 'deleteEmbeddedObject',
            'delete_filter_view': 'deleteFilterView',
            'delete_named_range': 'deleteNamedRange',
            'delete_protected_range': 'deleteProtectedRange',
            'delete_range': 'deleteRange',
            'delete_sheet': 'deleteSheet',
            'duplicate_filter_view': 'duplicateFilterView',
            'duplicate_sheet': 'duplicateSheet',
            'find_replace': 'findReplace',
            'insert_dimension': 'insertDimension',
            'insert_range': 'insertRange',
            'merge_cells': 'mergeCells',
            'move_dimension': 'moveDimension',
            'paste_data': 'pasteData',
            'randomize_range': 'randomizeRange',
            'refresh_data_source': 'refreshDataSource',
            'repeat_cell': 'repeatCell',
            'set_basic_filter': 'setBasicFilter',
            'set_data_validation': 'setDataValidation',
            'sort_range': 'sortRange',
            'text_to_columns': 'textToColumns',
            'trim_whitespace': 'trimWhitespace',
            'unmerge_cells': 'unmergeCells',
            'update_banding': 'updateBanding',
            'update_borders': 'updateBorders',
            'update_cells': 'updateCells',
            'update_chart_spec': 'updateChartSpec',
            'update_conditional_format_rule': 'updateConditionalFormatRule',
            'update_data_source': 'updateDataSource',
            'update_developer_metadata': 'updateDeveloperMetadata',
            'update_dimension_group': 'updateDimensionGroup',
            'update_dimension_properties': 'updateDimensionProperties',
            'update_embedded_object_border': 'updateEmbeddedObjectBorder',
            'update_embedded_object_position': 'updateEmbeddedObjectPosition',
            'update_filter_view': 'updateFilterView',
            'update_named_range': 'updateNamedRange',
            'update_protected_range': 'updateProtectedRange',
            'update_sheet_properties': 'updateSheetProperties',
            'update_slicer_spec': 'updateSlicerSpec',
            'update_spreadsheet_properties': 'updateSpreadsheetProperties'
        }

        self._add_banding = add_banding
        self._add_chart = add_chart
        self._add_conditional_format_rule = add_conditional_format_rule
        self._add_data_source = add_data_source
        self._add_dimension_group = add_dimension_group
        self._add_filter_view = add_filter_view
        self._add_named_range = add_named_range
        self._add_protected_range = add_protected_range
        self._add_sheet = add_sheet
        self._add_slicer = add_slicer
        self._append_cells = append_cells
        self._append_dimension = append_dimension
        self._auto_fill = auto_fill
        self._auto_resize_dimensions = auto_resize_dimensions
        self._clear_basic_filter = clear_basic_filter
        self._copy_paste = copy_paste
        self._create_developer_metadata = create_developer_metadata
        self._cut_paste = cut_paste
        self._delete_banding = delete_banding
        self._delete_conditional_format_rule = delete_conditional_format_rule
        self._delete_data_source = delete_data_source
        self._delete_developer_metadata = delete_developer_metadata
        self._delete_dimension = delete_dimension
        self._delete_dimension_group = delete_dimension_group
        self._delete_duplicates = delete_duplicates
        self._delete_embedded_object = delete_embedded_object
        self._delete_filter_view = delete_filter_view
        self._delete_named_range = delete_named_range
        self._delete_protected_range = delete_protected_range
        self._delete_range = delete_range
        self._delete_sheet = delete_sheet
        self._duplicate_filter_view = duplicate_filter_view
        self._duplicate_sheet = duplicate_sheet
        self._find_replace = find_replace
        self._insert_dimension = insert_dimension
        self._insert_range = insert_range
        self._merge_cells = merge_cells
        self._move_dimension = move_dimension
        self._paste_data = paste_data
        self._randomize_range = randomize_range
        self._refresh_data_source = refresh_data_source
        self._repeat_cell = repeat_cell
        self._set_basic_filter = set_basic_filter
        self._set_data_validation = set_data_validation
        self._sort_range = sort_range
        self._text_to_columns = text_to_columns
        self._trim_whitespace = trim_whitespace
        self._unmerge_cells = unmerge_cells
        self._update_banding = update_banding
        self._update_borders = update_borders
        self._update_cells = update_cells
        self._update_chart_spec = update_chart_spec
        self._update_conditional_format_rule = update_conditional_format_rule
        self._update_data_source = update_data_source
        self._update_developer_metadata = update_developer_metadata
        self._update_dimension_group = update_dimension_group
        self._update_dimension_properties = update_dimension_properties
        self._update_embedded_object_border = update_embedded_object_border
        self._update_embedded_object_position = update_embedded_object_position
        self._update_filter_view = update_filter_view
        self._update_named_range = update_named_range
        self._update_protected_range = update_protected_range
        self._update_sheet_properties = update_sheet_properties
        self._update_slicer_spec = update_slicer_spec
        self._update_spreadsheet_properties = update_spreadsheet_properties

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Request':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Request of this Request.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def add_banding(self):
        """Gets the add_banding of this Request.


        :return: The add_banding of this Request.
        :rtype: AddBandingRequest
        """
        return self._add_banding

    @add_banding.setter
    def add_banding(self, add_banding):
        """Sets the add_banding of this Request.


        :param add_banding: The add_banding of this Request.
        :type add_banding: AddBandingRequest
        """

        self._add_banding = add_banding

    @property
    def add_chart(self):
        """Gets the add_chart of this Request.


        :return: The add_chart of this Request.
        :rtype: AddChartRequest
        """
        return self._add_chart

    @add_chart.setter
    def add_chart(self, add_chart):
        """Sets the add_chart of this Request.


        :param add_chart: The add_chart of this Request.
        :type add_chart: AddChartRequest
        """

        self._add_chart = add_chart

    @property
    def add_conditional_format_rule(self):
        """Gets the add_conditional_format_rule of this Request.


        :return: The add_conditional_format_rule of this Request.
        :rtype: AddConditionalFormatRuleRequest
        """
        return self._add_conditional_format_rule

    @add_conditional_format_rule.setter
    def add_conditional_format_rule(self, add_conditional_format_rule):
        """Sets the add_conditional_format_rule of this Request.


        :param add_conditional_format_rule: The add_conditional_format_rule of this Request.
        :type add_conditional_format_rule: AddConditionalFormatRuleRequest
        """

        self._add_conditional_format_rule = add_conditional_format_rule

    @property
    def add_data_source(self):
        """Gets the add_data_source of this Request.


        :return: The add_data_source of this Request.
        :rtype: AddDataSourceRequest
        """
        return self._add_data_source

    @add_data_source.setter
    def add_data_source(self, add_data_source):
        """Sets the add_data_source of this Request.


        :param add_data_source: The add_data_source of this Request.
        :type add_data_source: AddDataSourceRequest
        """

        self._add_data_source = add_data_source

    @property
    def add_dimension_group(self):
        """Gets the add_dimension_group of this Request.


        :return: The add_dimension_group of this Request.
        :rtype: AddDimensionGroupRequest
        """
        return self._add_dimension_group

    @add_dimension_group.setter
    def add_dimension_group(self, add_dimension_group):
        """Sets the add_dimension_group of this Request.


        :param add_dimension_group: The add_dimension_group of this Request.
        :type add_dimension_group: AddDimensionGroupRequest
        """

        self._add_dimension_group = add_dimension_group

    @property
    def add_filter_view(self):
        """Gets the add_filter_view of this Request.


        :return: The add_filter_view of this Request.
        :rtype: AddFilterViewRequest
        """
        return self._add_filter_view

    @add_filter_view.setter
    def add_filter_view(self, add_filter_view):
        """Sets the add_filter_view of this Request.


        :param add_filter_view: The add_filter_view of this Request.
        :type add_filter_view: AddFilterViewRequest
        """

        self._add_filter_view = add_filter_view

    @property
    def add_named_range(self):
        """Gets the add_named_range of this Request.


        :return: The add_named_range of this Request.
        :rtype: AddNamedRangeRequest
        """
        return self._add_named_range

    @add_named_range.setter
    def add_named_range(self, add_named_range):
        """Sets the add_named_range of this Request.


        :param add_named_range: The add_named_range of this Request.
        :type add_named_range: AddNamedRangeRequest
        """

        self._add_named_range = add_named_range

    @property
    def add_protected_range(self):
        """Gets the add_protected_range of this Request.


        :return: The add_protected_range of this Request.
        :rtype: AddProtectedRangeRequest
        """
        return self._add_protected_range

    @add_protected_range.setter
    def add_protected_range(self, add_protected_range):
        """Sets the add_protected_range of this Request.


        :param add_protected_range: The add_protected_range of this Request.
        :type add_protected_range: AddProtectedRangeRequest
        """

        self._add_protected_range = add_protected_range

    @property
    def add_sheet(self):
        """Gets the add_sheet of this Request.


        :return: The add_sheet of this Request.
        :rtype: AddSheetRequest
        """
        return self._add_sheet

    @add_sheet.setter
    def add_sheet(self, add_sheet):
        """Sets the add_sheet of this Request.


        :param add_sheet: The add_sheet of this Request.
        :type add_sheet: AddSheetRequest
        """

        self._add_sheet = add_sheet

    @property
    def add_slicer(self):
        """Gets the add_slicer of this Request.


        :return: The add_slicer of this Request.
        :rtype: AddSlicerRequest
        """
        return self._add_slicer

    @add_slicer.setter
    def add_slicer(self, add_slicer):
        """Sets the add_slicer of this Request.


        :param add_slicer: The add_slicer of this Request.
        :type add_slicer: AddSlicerRequest
        """

        self._add_slicer = add_slicer

    @property
    def append_cells(self):
        """Gets the append_cells of this Request.


        :return: The append_cells of this Request.
        :rtype: AppendCellsRequest
        """
        return self._append_cells

    @append_cells.setter
    def append_cells(self, append_cells):
        """Sets the append_cells of this Request.


        :param append_cells: The append_cells of this Request.
        :type append_cells: AppendCellsRequest
        """

        self._append_cells = append_cells

    @property
    def append_dimension(self):
        """Gets the append_dimension of this Request.


        :return: The append_dimension of this Request.
        :rtype: AppendDimensionRequest
        """
        return self._append_dimension

    @append_dimension.setter
    def append_dimension(self, append_dimension):
        """Sets the append_dimension of this Request.


        :param append_dimension: The append_dimension of this Request.
        :type append_dimension: AppendDimensionRequest
        """

        self._append_dimension = append_dimension

    @property
    def auto_fill(self):
        """Gets the auto_fill of this Request.


        :return: The auto_fill of this Request.
        :rtype: AutoFillRequest
        """
        return self._auto_fill

    @auto_fill.setter
    def auto_fill(self, auto_fill):
        """Sets the auto_fill of this Request.


        :param auto_fill: The auto_fill of this Request.
        :type auto_fill: AutoFillRequest
        """

        self._auto_fill = auto_fill

    @property
    def auto_resize_dimensions(self):
        """Gets the auto_resize_dimensions of this Request.


        :return: The auto_resize_dimensions of this Request.
        :rtype: AutoResizeDimensionsRequest
        """
        return self._auto_resize_dimensions

    @auto_resize_dimensions.setter
    def auto_resize_dimensions(self, auto_resize_dimensions):
        """Sets the auto_resize_dimensions of this Request.


        :param auto_resize_dimensions: The auto_resize_dimensions of this Request.
        :type auto_resize_dimensions: AutoResizeDimensionsRequest
        """

        self._auto_resize_dimensions = auto_resize_dimensions

    @property
    def clear_basic_filter(self):
        """Gets the clear_basic_filter of this Request.


        :return: The clear_basic_filter of this Request.
        :rtype: ClearBasicFilterRequest
        """
        return self._clear_basic_filter

    @clear_basic_filter.setter
    def clear_basic_filter(self, clear_basic_filter):
        """Sets the clear_basic_filter of this Request.


        :param clear_basic_filter: The clear_basic_filter of this Request.
        :type clear_basic_filter: ClearBasicFilterRequest
        """

        self._clear_basic_filter = clear_basic_filter

    @property
    def copy_paste(self):
        """Gets the copy_paste of this Request.


        :return: The copy_paste of this Request.
        :rtype: CopyPasteRequest
        """
        return self._copy_paste

    @copy_paste.setter
    def copy_paste(self, copy_paste):
        """Sets the copy_paste of this Request.


        :param copy_paste: The copy_paste of this Request.
        :type copy_paste: CopyPasteRequest
        """

        self._copy_paste = copy_paste

    @property
    def create_developer_metadata(self):
        """Gets the create_developer_metadata of this Request.


        :return: The create_developer_metadata of this Request.
        :rtype: CreateDeveloperMetadataRequest
        """
        return self._create_developer_metadata

    @create_developer_metadata.setter
    def create_developer_metadata(self, create_developer_metadata):
        """Sets the create_developer_metadata of this Request.


        :param create_developer_metadata: The create_developer_metadata of this Request.
        :type create_developer_metadata: CreateDeveloperMetadataRequest
        """

        self._create_developer_metadata = create_developer_metadata

    @property
    def cut_paste(self):
        """Gets the cut_paste of this Request.


        :return: The cut_paste of this Request.
        :rtype: CutPasteRequest
        """
        return self._cut_paste

    @cut_paste.setter
    def cut_paste(self, cut_paste):
        """Sets the cut_paste of this Request.


        :param cut_paste: The cut_paste of this Request.
        :type cut_paste: CutPasteRequest
        """

        self._cut_paste = cut_paste

    @property
    def delete_banding(self):
        """Gets the delete_banding of this Request.


        :return: The delete_banding of this Request.
        :rtype: DeleteBandingRequest
        """
        return self._delete_banding

    @delete_banding.setter
    def delete_banding(self, delete_banding):
        """Sets the delete_banding of this Request.


        :param delete_banding: The delete_banding of this Request.
        :type delete_banding: DeleteBandingRequest
        """

        self._delete_banding = delete_banding

    @property
    def delete_conditional_format_rule(self):
        """Gets the delete_conditional_format_rule of this Request.


        :return: The delete_conditional_format_rule of this Request.
        :rtype: DeleteConditionalFormatRuleRequest
        """
        return self._delete_conditional_format_rule

    @delete_conditional_format_rule.setter
    def delete_conditional_format_rule(self, delete_conditional_format_rule):
        """Sets the delete_conditional_format_rule of this Request.


        :param delete_conditional_format_rule: The delete_conditional_format_rule of this Request.
        :type delete_conditional_format_rule: DeleteConditionalFormatRuleRequest
        """

        self._delete_conditional_format_rule = delete_conditional_format_rule

    @property
    def delete_data_source(self):
        """Gets the delete_data_source of this Request.


        :return: The delete_data_source of this Request.
        :rtype: DeleteDataSourceRequest
        """
        return self._delete_data_source

    @delete_data_source.setter
    def delete_data_source(self, delete_data_source):
        """Sets the delete_data_source of this Request.


        :param delete_data_source: The delete_data_source of this Request.
        :type delete_data_source: DeleteDataSourceRequest
        """

        self._delete_data_source = delete_data_source

    @property
    def delete_developer_metadata(self):
        """Gets the delete_developer_metadata of this Request.


        :return: The delete_developer_metadata of this Request.
        :rtype: DeleteDeveloperMetadataRequest
        """
        return self._delete_developer_metadata

    @delete_developer_metadata.setter
    def delete_developer_metadata(self, delete_developer_metadata):
        """Sets the delete_developer_metadata of this Request.


        :param delete_developer_metadata: The delete_developer_metadata of this Request.
        :type delete_developer_metadata: DeleteDeveloperMetadataRequest
        """

        self._delete_developer_metadata = delete_developer_metadata

    @property
    def delete_dimension(self):
        """Gets the delete_dimension of this Request.


        :return: The delete_dimension of this Request.
        :rtype: DeleteDimensionRequest
        """
        return self._delete_dimension

    @delete_dimension.setter
    def delete_dimension(self, delete_dimension):
        """Sets the delete_dimension of this Request.


        :param delete_dimension: The delete_dimension of this Request.
        :type delete_dimension: DeleteDimensionRequest
        """

        self._delete_dimension = delete_dimension

    @property
    def delete_dimension_group(self):
        """Gets the delete_dimension_group of this Request.


        :return: The delete_dimension_group of this Request.
        :rtype: DeleteDimensionGroupRequest
        """
        return self._delete_dimension_group

    @delete_dimension_group.setter
    def delete_dimension_group(self, delete_dimension_group):
        """Sets the delete_dimension_group of this Request.


        :param delete_dimension_group: The delete_dimension_group of this Request.
        :type delete_dimension_group: DeleteDimensionGroupRequest
        """

        self._delete_dimension_group = delete_dimension_group

    @property
    def delete_duplicates(self):
        """Gets the delete_duplicates of this Request.


        :return: The delete_duplicates of this Request.
        :rtype: DeleteDuplicatesRequest
        """
        return self._delete_duplicates

    @delete_duplicates.setter
    def delete_duplicates(self, delete_duplicates):
        """Sets the delete_duplicates of this Request.


        :param delete_duplicates: The delete_duplicates of this Request.
        :type delete_duplicates: DeleteDuplicatesRequest
        """

        self._delete_duplicates = delete_duplicates

    @property
    def delete_embedded_object(self):
        """Gets the delete_embedded_object of this Request.


        :return: The delete_embedded_object of this Request.
        :rtype: DeleteEmbeddedObjectRequest
        """
        return self._delete_embedded_object

    @delete_embedded_object.setter
    def delete_embedded_object(self, delete_embedded_object):
        """Sets the delete_embedded_object of this Request.


        :param delete_embedded_object: The delete_embedded_object of this Request.
        :type delete_embedded_object: DeleteEmbeddedObjectRequest
        """

        self._delete_embedded_object = delete_embedded_object

    @property
    def delete_filter_view(self):
        """Gets the delete_filter_view of this Request.


        :return: The delete_filter_view of this Request.
        :rtype: DeleteFilterViewRequest
        """
        return self._delete_filter_view

    @delete_filter_view.setter
    def delete_filter_view(self, delete_filter_view):
        """Sets the delete_filter_view of this Request.


        :param delete_filter_view: The delete_filter_view of this Request.
        :type delete_filter_view: DeleteFilterViewRequest
        """

        self._delete_filter_view = delete_filter_view

    @property
    def delete_named_range(self):
        """Gets the delete_named_range of this Request.


        :return: The delete_named_range of this Request.
        :rtype: DeleteNamedRangeRequest
        """
        return self._delete_named_range

    @delete_named_range.setter
    def delete_named_range(self, delete_named_range):
        """Sets the delete_named_range of this Request.


        :param delete_named_range: The delete_named_range of this Request.
        :type delete_named_range: DeleteNamedRangeRequest
        """

        self._delete_named_range = delete_named_range

    @property
    def delete_protected_range(self):
        """Gets the delete_protected_range of this Request.


        :return: The delete_protected_range of this Request.
        :rtype: DeleteProtectedRangeRequest
        """
        return self._delete_protected_range

    @delete_protected_range.setter
    def delete_protected_range(self, delete_protected_range):
        """Sets the delete_protected_range of this Request.


        :param delete_protected_range: The delete_protected_range of this Request.
        :type delete_protected_range: DeleteProtectedRangeRequest
        """

        self._delete_protected_range = delete_protected_range

    @property
    def delete_range(self):
        """Gets the delete_range of this Request.


        :return: The delete_range of this Request.
        :rtype: DeleteRangeRequest
        """
        return self._delete_range

    @delete_range.setter
    def delete_range(self, delete_range):
        """Sets the delete_range of this Request.


        :param delete_range: The delete_range of this Request.
        :type delete_range: DeleteRangeRequest
        """

        self._delete_range = delete_range

    @property
    def delete_sheet(self):
        """Gets the delete_sheet of this Request.


        :return: The delete_sheet of this Request.
        :rtype: DeleteSheetRequest
        """
        return self._delete_sheet

    @delete_sheet.setter
    def delete_sheet(self, delete_sheet):
        """Sets the delete_sheet of this Request.


        :param delete_sheet: The delete_sheet of this Request.
        :type delete_sheet: DeleteSheetRequest
        """

        self._delete_sheet = delete_sheet

    @property
    def duplicate_filter_view(self):
        """Gets the duplicate_filter_view of this Request.


        :return: The duplicate_filter_view of this Request.
        :rtype: DuplicateFilterViewRequest
        """
        return self._duplicate_filter_view

    @duplicate_filter_view.setter
    def duplicate_filter_view(self, duplicate_filter_view):
        """Sets the duplicate_filter_view of this Request.


        :param duplicate_filter_view: The duplicate_filter_view of this Request.
        :type duplicate_filter_view: DuplicateFilterViewRequest
        """

        self._duplicate_filter_view = duplicate_filter_view

    @property
    def duplicate_sheet(self):
        """Gets the duplicate_sheet of this Request.


        :return: The duplicate_sheet of this Request.
        :rtype: DuplicateSheetRequest
        """
        return self._duplicate_sheet

    @duplicate_sheet.setter
    def duplicate_sheet(self, duplicate_sheet):
        """Sets the duplicate_sheet of this Request.


        :param duplicate_sheet: The duplicate_sheet of this Request.
        :type duplicate_sheet: DuplicateSheetRequest
        """

        self._duplicate_sheet = duplicate_sheet

    @property
    def find_replace(self):
        """Gets the find_replace of this Request.


        :return: The find_replace of this Request.
        :rtype: FindReplaceRequest
        """
        return self._find_replace

    @find_replace.setter
    def find_replace(self, find_replace):
        """Sets the find_replace of this Request.


        :param find_replace: The find_replace of this Request.
        :type find_replace: FindReplaceRequest
        """

        self._find_replace = find_replace

    @property
    def insert_dimension(self):
        """Gets the insert_dimension of this Request.


        :return: The insert_dimension of this Request.
        :rtype: InsertDimensionRequest
        """
        return self._insert_dimension

    @insert_dimension.setter
    def insert_dimension(self, insert_dimension):
        """Sets the insert_dimension of this Request.


        :param insert_dimension: The insert_dimension of this Request.
        :type insert_dimension: InsertDimensionRequest
        """

        self._insert_dimension = insert_dimension

    @property
    def insert_range(self):
        """Gets the insert_range of this Request.


        :return: The insert_range of this Request.
        :rtype: InsertRangeRequest
        """
        return self._insert_range

    @insert_range.setter
    def insert_range(self, insert_range):
        """Sets the insert_range of this Request.


        :param insert_range: The insert_range of this Request.
        :type insert_range: InsertRangeRequest
        """

        self._insert_range = insert_range

    @property
    def merge_cells(self):
        """Gets the merge_cells of this Request.


        :return: The merge_cells of this Request.
        :rtype: MergeCellsRequest
        """
        return self._merge_cells

    @merge_cells.setter
    def merge_cells(self, merge_cells):
        """Sets the merge_cells of this Request.


        :param merge_cells: The merge_cells of this Request.
        :type merge_cells: MergeCellsRequest
        """

        self._merge_cells = merge_cells

    @property
    def move_dimension(self):
        """Gets the move_dimension of this Request.


        :return: The move_dimension of this Request.
        :rtype: MoveDimensionRequest
        """
        return self._move_dimension

    @move_dimension.setter
    def move_dimension(self, move_dimension):
        """Sets the move_dimension of this Request.


        :param move_dimension: The move_dimension of this Request.
        :type move_dimension: MoveDimensionRequest
        """

        self._move_dimension = move_dimension

    @property
    def paste_data(self):
        """Gets the paste_data of this Request.


        :return: The paste_data of this Request.
        :rtype: PasteDataRequest
        """
        return self._paste_data

    @paste_data.setter
    def paste_data(self, paste_data):
        """Sets the paste_data of this Request.


        :param paste_data: The paste_data of this Request.
        :type paste_data: PasteDataRequest
        """

        self._paste_data = paste_data

    @property
    def randomize_range(self):
        """Gets the randomize_range of this Request.


        :return: The randomize_range of this Request.
        :rtype: RandomizeRangeRequest
        """
        return self._randomize_range

    @randomize_range.setter
    def randomize_range(self, randomize_range):
        """Sets the randomize_range of this Request.


        :param randomize_range: The randomize_range of this Request.
        :type randomize_range: RandomizeRangeRequest
        """

        self._randomize_range = randomize_range

    @property
    def refresh_data_source(self):
        """Gets the refresh_data_source of this Request.


        :return: The refresh_data_source of this Request.
        :rtype: RefreshDataSourceRequest
        """
        return self._refresh_data_source

    @refresh_data_source.setter
    def refresh_data_source(self, refresh_data_source):
        """Sets the refresh_data_source of this Request.


        :param refresh_data_source: The refresh_data_source of this Request.
        :type refresh_data_source: RefreshDataSourceRequest
        """

        self._refresh_data_source = refresh_data_source

    @property
    def repeat_cell(self):
        """Gets the repeat_cell of this Request.


        :return: The repeat_cell of this Request.
        :rtype: RepeatCellRequest
        """
        return self._repeat_cell

    @repeat_cell.setter
    def repeat_cell(self, repeat_cell):
        """Sets the repeat_cell of this Request.


        :param repeat_cell: The repeat_cell of this Request.
        :type repeat_cell: RepeatCellRequest
        """

        self._repeat_cell = repeat_cell

    @property
    def set_basic_filter(self):
        """Gets the set_basic_filter of this Request.


        :return: The set_basic_filter of this Request.
        :rtype: SetBasicFilterRequest
        """
        return self._set_basic_filter

    @set_basic_filter.setter
    def set_basic_filter(self, set_basic_filter):
        """Sets the set_basic_filter of this Request.


        :param set_basic_filter: The set_basic_filter of this Request.
        :type set_basic_filter: SetBasicFilterRequest
        """

        self._set_basic_filter = set_basic_filter

    @property
    def set_data_validation(self):
        """Gets the set_data_validation of this Request.


        :return: The set_data_validation of this Request.
        :rtype: SetDataValidationRequest
        """
        return self._set_data_validation

    @set_data_validation.setter
    def set_data_validation(self, set_data_validation):
        """Sets the set_data_validation of this Request.


        :param set_data_validation: The set_data_validation of this Request.
        :type set_data_validation: SetDataValidationRequest
        """

        self._set_data_validation = set_data_validation

    @property
    def sort_range(self):
        """Gets the sort_range of this Request.


        :return: The sort_range of this Request.
        :rtype: SortRangeRequest
        """
        return self._sort_range

    @sort_range.setter
    def sort_range(self, sort_range):
        """Sets the sort_range of this Request.


        :param sort_range: The sort_range of this Request.
        :type sort_range: SortRangeRequest
        """

        self._sort_range = sort_range

    @property
    def text_to_columns(self):
        """Gets the text_to_columns of this Request.


        :return: The text_to_columns of this Request.
        :rtype: TextToColumnsRequest
        """
        return self._text_to_columns

    @text_to_columns.setter
    def text_to_columns(self, text_to_columns):
        """Sets the text_to_columns of this Request.


        :param text_to_columns: The text_to_columns of this Request.
        :type text_to_columns: TextToColumnsRequest
        """

        self._text_to_columns = text_to_columns

    @property
    def trim_whitespace(self):
        """Gets the trim_whitespace of this Request.


        :return: The trim_whitespace of this Request.
        :rtype: TrimWhitespaceRequest
        """
        return self._trim_whitespace

    @trim_whitespace.setter
    def trim_whitespace(self, trim_whitespace):
        """Sets the trim_whitespace of this Request.


        :param trim_whitespace: The trim_whitespace of this Request.
        :type trim_whitespace: TrimWhitespaceRequest
        """

        self._trim_whitespace = trim_whitespace

    @property
    def unmerge_cells(self):
        """Gets the unmerge_cells of this Request.


        :return: The unmerge_cells of this Request.
        :rtype: UnmergeCellsRequest
        """
        return self._unmerge_cells

    @unmerge_cells.setter
    def unmerge_cells(self, unmerge_cells):
        """Sets the unmerge_cells of this Request.


        :param unmerge_cells: The unmerge_cells of this Request.
        :type unmerge_cells: UnmergeCellsRequest
        """

        self._unmerge_cells = unmerge_cells

    @property
    def update_banding(self):
        """Gets the update_banding of this Request.


        :return: The update_banding of this Request.
        :rtype: UpdateBandingRequest
        """
        return self._update_banding

    @update_banding.setter
    def update_banding(self, update_banding):
        """Sets the update_banding of this Request.


        :param update_banding: The update_banding of this Request.
        :type update_banding: UpdateBandingRequest
        """

        self._update_banding = update_banding

    @property
    def update_borders(self):
        """Gets the update_borders of this Request.


        :return: The update_borders of this Request.
        :rtype: UpdateBordersRequest
        """
        return self._update_borders

    @update_borders.setter
    def update_borders(self, update_borders):
        """Sets the update_borders of this Request.


        :param update_borders: The update_borders of this Request.
        :type update_borders: UpdateBordersRequest
        """

        self._update_borders = update_borders

    @property
    def update_cells(self):
        """Gets the update_cells of this Request.


        :return: The update_cells of this Request.
        :rtype: UpdateCellsRequest
        """
        return self._update_cells

    @update_cells.setter
    def update_cells(self, update_cells):
        """Sets the update_cells of this Request.


        :param update_cells: The update_cells of this Request.
        :type update_cells: UpdateCellsRequest
        """

        self._update_cells = update_cells

    @property
    def update_chart_spec(self):
        """Gets the update_chart_spec of this Request.


        :return: The update_chart_spec of this Request.
        :rtype: UpdateChartSpecRequest
        """
        return self._update_chart_spec

    @update_chart_spec.setter
    def update_chart_spec(self, update_chart_spec):
        """Sets the update_chart_spec of this Request.


        :param update_chart_spec: The update_chart_spec of this Request.
        :type update_chart_spec: UpdateChartSpecRequest
        """

        self._update_chart_spec = update_chart_spec

    @property
    def update_conditional_format_rule(self):
        """Gets the update_conditional_format_rule of this Request.


        :return: The update_conditional_format_rule of this Request.
        :rtype: UpdateConditionalFormatRuleRequest
        """
        return self._update_conditional_format_rule

    @update_conditional_format_rule.setter
    def update_conditional_format_rule(self, update_conditional_format_rule):
        """Sets the update_conditional_format_rule of this Request.


        :param update_conditional_format_rule: The update_conditional_format_rule of this Request.
        :type update_conditional_format_rule: UpdateConditionalFormatRuleRequest
        """

        self._update_conditional_format_rule = update_conditional_format_rule

    @property
    def update_data_source(self):
        """Gets the update_data_source of this Request.


        :return: The update_data_source of this Request.
        :rtype: UpdateDataSourceRequest
        """
        return self._update_data_source

    @update_data_source.setter
    def update_data_source(self, update_data_source):
        """Sets the update_data_source of this Request.


        :param update_data_source: The update_data_source of this Request.
        :type update_data_source: UpdateDataSourceRequest
        """

        self._update_data_source = update_data_source

    @property
    def update_developer_metadata(self):
        """Gets the update_developer_metadata of this Request.


        :return: The update_developer_metadata of this Request.
        :rtype: UpdateDeveloperMetadataRequest
        """
        return self._update_developer_metadata

    @update_developer_metadata.setter
    def update_developer_metadata(self, update_developer_metadata):
        """Sets the update_developer_metadata of this Request.


        :param update_developer_metadata: The update_developer_metadata of this Request.
        :type update_developer_metadata: UpdateDeveloperMetadataRequest
        """

        self._update_developer_metadata = update_developer_metadata

    @property
    def update_dimension_group(self):
        """Gets the update_dimension_group of this Request.


        :return: The update_dimension_group of this Request.
        :rtype: UpdateDimensionGroupRequest
        """
        return self._update_dimension_group

    @update_dimension_group.setter
    def update_dimension_group(self, update_dimension_group):
        """Sets the update_dimension_group of this Request.


        :param update_dimension_group: The update_dimension_group of this Request.
        :type update_dimension_group: UpdateDimensionGroupRequest
        """

        self._update_dimension_group = update_dimension_group

    @property
    def update_dimension_properties(self):
        """Gets the update_dimension_properties of this Request.


        :return: The update_dimension_properties of this Request.
        :rtype: UpdateDimensionPropertiesRequest
        """
        return self._update_dimension_properties

    @update_dimension_properties.setter
    def update_dimension_properties(self, update_dimension_properties):
        """Sets the update_dimension_properties of this Request.


        :param update_dimension_properties: The update_dimension_properties of this Request.
        :type update_dimension_properties: UpdateDimensionPropertiesRequest
        """

        self._update_dimension_properties = update_dimension_properties

    @property
    def update_embedded_object_border(self):
        """Gets the update_embedded_object_border of this Request.


        :return: The update_embedded_object_border of this Request.
        :rtype: UpdateEmbeddedObjectBorderRequest
        """
        return self._update_embedded_object_border

    @update_embedded_object_border.setter
    def update_embedded_object_border(self, update_embedded_object_border):
        """Sets the update_embedded_object_border of this Request.


        :param update_embedded_object_border: The update_embedded_object_border of this Request.
        :type update_embedded_object_border: UpdateEmbeddedObjectBorderRequest
        """

        self._update_embedded_object_border = update_embedded_object_border

    @property
    def update_embedded_object_position(self):
        """Gets the update_embedded_object_position of this Request.


        :return: The update_embedded_object_position of this Request.
        :rtype: UpdateEmbeddedObjectPositionRequest
        """
        return self._update_embedded_object_position

    @update_embedded_object_position.setter
    def update_embedded_object_position(self, update_embedded_object_position):
        """Sets the update_embedded_object_position of this Request.


        :param update_embedded_object_position: The update_embedded_object_position of this Request.
        :type update_embedded_object_position: UpdateEmbeddedObjectPositionRequest
        """

        self._update_embedded_object_position = update_embedded_object_position

    @property
    def update_filter_view(self):
        """Gets the update_filter_view of this Request.


        :return: The update_filter_view of this Request.
        :rtype: UpdateFilterViewRequest
        """
        return self._update_filter_view

    @update_filter_view.setter
    def update_filter_view(self, update_filter_view):
        """Sets the update_filter_view of this Request.


        :param update_filter_view: The update_filter_view of this Request.
        :type update_filter_view: UpdateFilterViewRequest
        """

        self._update_filter_view = update_filter_view

    @property
    def update_named_range(self):
        """Gets the update_named_range of this Request.


        :return: The update_named_range of this Request.
        :rtype: UpdateNamedRangeRequest
        """
        return self._update_named_range

    @update_named_range.setter
    def update_named_range(self, update_named_range):
        """Sets the update_named_range of this Request.


        :param update_named_range: The update_named_range of this Request.
        :type update_named_range: UpdateNamedRangeRequest
        """

        self._update_named_range = update_named_range

    @property
    def update_protected_range(self):
        """Gets the update_protected_range of this Request.


        :return: The update_protected_range of this Request.
        :rtype: UpdateProtectedRangeRequest
        """
        return self._update_protected_range

    @update_protected_range.setter
    def update_protected_range(self, update_protected_range):
        """Sets the update_protected_range of this Request.


        :param update_protected_range: The update_protected_range of this Request.
        :type update_protected_range: UpdateProtectedRangeRequest
        """

        self._update_protected_range = update_protected_range

    @property
    def update_sheet_properties(self):
        """Gets the update_sheet_properties of this Request.


        :return: The update_sheet_properties of this Request.
        :rtype: UpdateSheetPropertiesRequest
        """
        return self._update_sheet_properties

    @update_sheet_properties.setter
    def update_sheet_properties(self, update_sheet_properties):
        """Sets the update_sheet_properties of this Request.


        :param update_sheet_properties: The update_sheet_properties of this Request.
        :type update_sheet_properties: UpdateSheetPropertiesRequest
        """

        self._update_sheet_properties = update_sheet_properties

    @property
    def update_slicer_spec(self):
        """Gets the update_slicer_spec of this Request.


        :return: The update_slicer_spec of this Request.
        :rtype: UpdateSlicerSpecRequest
        """
        return self._update_slicer_spec

    @update_slicer_spec.setter
    def update_slicer_spec(self, update_slicer_spec):
        """Sets the update_slicer_spec of this Request.


        :param update_slicer_spec: The update_slicer_spec of this Request.
        :type update_slicer_spec: UpdateSlicerSpecRequest
        """

        self._update_slicer_spec = update_slicer_spec

    @property
    def update_spreadsheet_properties(self):
        """Gets the update_spreadsheet_properties of this Request.


        :return: The update_spreadsheet_properties of this Request.
        :rtype: UpdateSpreadsheetPropertiesRequest
        """
        return self._update_spreadsheet_properties

    @update_spreadsheet_properties.setter
    def update_spreadsheet_properties(self, update_spreadsheet_properties):
        """Sets the update_spreadsheet_properties of this Request.


        :param update_spreadsheet_properties: The update_spreadsheet_properties of this Request.
        :type update_spreadsheet_properties: UpdateSpreadsheetPropertiesRequest
        """

        self._update_spreadsheet_properties = update_spreadsheet_properties
