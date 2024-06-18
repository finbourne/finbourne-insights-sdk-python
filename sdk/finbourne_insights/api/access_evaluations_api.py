# coding: utf-8

"""
    FINBOURNE Insights API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.783
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from finbourne_insights.api_client import ApiClient
from finbourne_insights.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)
from finbourne_insights.models.access_evaluation_log import AccessEvaluationLog
from finbourne_insights.models.lusid_problem_details import LusidProblemDetails
from finbourne_insights.models.lusid_validation_problem_details import LusidValidationProblemDetails
from finbourne_insights.models.resource_list_with_histogram_of_access_evaluation_log import ResourceListWithHistogramOfAccessEvaluationLog


class AccessEvaluationsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_access_evaluation_log(self, id, **kwargs):  # noqa: E501
        """[EARLY ACCESS] GetAccessEvaluationLog: Get the log for a specific access evaluation.  This endpoint will be deprecated in the near future.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_access_evaluation_log(id, async_req=True)
        >>> result = thread.get()

        :param id: The identifier of the access evaluation to obtain the log for. (required)
        :type id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AccessEvaluationLog
        """
        kwargs['_return_http_data_only'] = True
        return self.get_access_evaluation_log_with_http_info(id, **kwargs)  # noqa: E501

    def get_access_evaluation_log_with_http_info(self, id, **kwargs):  # noqa: E501
        """[EARLY ACCESS] GetAccessEvaluationLog: Get the log for a specific access evaluation.  This endpoint will be deprecated in the near future.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_access_evaluation_log_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param id: The identifier of the access evaluation to obtain the log for. (required)
        :type id: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object, the HTTP status code, and the headers.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: (AccessEvaluationLog, int, HTTPHeaderDict)
        """

        local_var_params = locals()

        all_params = [
            'id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_access_evaluation_log" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `get_access_evaluation_log`")  # noqa: E501

        if self.api_client.client_side_validation and ('id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['id']) > 70):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `id` when calling `get_access_evaluation_log`, length must be less than or equal to `70`")  # noqa: E501
        if self.api_client.client_side_validation and ('id' in local_var_params and  # noqa: E501
                                                        len(local_var_params['id']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `id` when calling `get_access_evaluation_log`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'id' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_:\+]+$', local_var_params['id']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `id` when calling `get_access_evaluation_log`, must conform to the pattern `/^[a-zA-Z0-9\-_:\+]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'id' in local_var_params:
            path_params['id'] = local_var_params['id']  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        header_params['Accept-Encoding'] = "gzip, deflate, br"


        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.0.783'

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        response_types_map = {
            200: "AccessEvaluationLog",
            400: "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/access/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def list_access_evaluation_logs(self, **kwargs):  # noqa: E501
        """[EARLY ACCESS] ListAccessEvaluationLogs: List the logs for access evaluations.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_access_evaluation_logs(async_req=True)
        >>> result = thread.get()

        :param start_at: Start date from which point to fetch logs.
        :type start_at: datetime
        :param end_at: End date to which point to fetch logs.
        :type end_at: datetime
        :param filter: Expression to filter the result set. Read more about <see href=\"https://support.lusid.com/filtering-results-from-lusid\"> filtering results from LUSID</see>.
        :type filter: str
        :param sort_by: Order the results by these fields. Use the '-' sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName
        :type sort_by: str
        :param limit: When paginating, only return this number of records. The minimum value is 0 and the maximum is 10000.
        :type limit: int
        :param page: Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter and sortby fields should not be supplied.
        :type page: str
        :param histogram_interval: The interval for an included histogram of the logs
        :type histogram_interval: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ResourceListWithHistogramOfAccessEvaluationLog
        """
        kwargs['_return_http_data_only'] = True
        return self.list_access_evaluation_logs_with_http_info(**kwargs)  # noqa: E501

    def list_access_evaluation_logs_with_http_info(self, **kwargs):  # noqa: E501
        """[EARLY ACCESS] ListAccessEvaluationLogs: List the logs for access evaluations.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_access_evaluation_logs_with_http_info(async_req=True)
        >>> result = thread.get()

        :param start_at: Start date from which point to fetch logs.
        :type start_at: datetime
        :param end_at: End date to which point to fetch logs.
        :type end_at: datetime
        :param filter: Expression to filter the result set. Read more about <see href=\"https://support.lusid.com/filtering-results-from-lusid\"> filtering results from LUSID</see>.
        :type filter: str
        :param sort_by: Order the results by these fields. Use the '-' sign to denote descending order e.g. -MyFieldName. Multiple fields can be denoted by a comma e.g. -MyFieldName,AnotherFieldName,-AFurtherFieldName
        :type sort_by: str
        :param limit: When paginating, only return this number of records. The minimum value is 0 and the maximum is 10000.
        :type limit: int
        :param page: Encoded page string returned from a previous search result that will retrieve the next page of data. When this field is supplied, filter and sortby fields should not be supplied.
        :type page: str
        :param histogram_interval: The interval for an included histogram of the logs
        :type histogram_interval: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object, the HTTP status code, and the headers.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: (ResourceListWithHistogramOfAccessEvaluationLog, int, HTTPHeaderDict)
        """

        local_var_params = locals()

        all_params = [
            'start_at',
            'end_at',
            'filter',
            'sort_by',
            'limit',
            'page',
            'histogram_interval'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_access_evaluation_logs" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and ('filter' in local_var_params and  # noqa: E501
                                                        len(local_var_params['filter']) > 16384):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `filter` when calling `list_access_evaluation_logs`, length must be less than or equal to `16384`")  # noqa: E501
        if self.api_client.client_side_validation and ('filter' in local_var_params and  # noqa: E501
                                                        len(local_var_params['filter']) < 0):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `filter` when calling `list_access_evaluation_logs`, length must be greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and 'filter' in local_var_params and not re.search(r'^[\s\S]*$', local_var_params['filter']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `filter` when calling `list_access_evaluation_logs`, must conform to the pattern `/^[\s\S]*$/`")  # noqa: E501
        if self.api_client.client_side_validation and ('sort_by' in local_var_params and  # noqa: E501
                                                        len(local_var_params['sort_by']) > 16384):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `sort_by` when calling `list_access_evaluation_logs`, length must be less than or equal to `16384`")  # noqa: E501
        if self.api_client.client_side_validation and ('sort_by' in local_var_params and  # noqa: E501
                                                        len(local_var_params['sort_by']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `sort_by` when calling `list_access_evaluation_logs`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'sort_by' in local_var_params and not re.search(r'^[\s\S]*$', local_var_params['sort_by']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `sort_by` when calling `list_access_evaluation_logs`, must conform to the pattern `/^[\s\S]*$/`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 10000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `list_access_evaluation_logs`, must be a value less than or equal to `10000`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `list_access_evaluation_logs`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('page' in local_var_params and  # noqa: E501
                                                        len(local_var_params['page']) > 500):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page` when calling `list_access_evaluation_logs`, length must be less than or equal to `500`")  # noqa: E501
        if self.api_client.client_side_validation and ('page' in local_var_params and  # noqa: E501
                                                        len(local_var_params['page']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page` when calling `list_access_evaluation_logs`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'page' in local_var_params and not re.search(r'^[a-zA-Z0-9\+\/]*={0,3}$', local_var_params['page']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page` when calling `list_access_evaluation_logs`, must conform to the pattern `/^[a-zA-Z0-9\+\/]*={0,3}$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_at' in local_var_params and local_var_params['start_at'] is not None:  # noqa: E501
            query_params.append(('startAt', local_var_params['start_at']))  # noqa: E501
        if 'end_at' in local_var_params and local_var_params['end_at'] is not None:  # noqa: E501
            query_params.append(('endAt', local_var_params['end_at']))  # noqa: E501
        if 'filter' in local_var_params and local_var_params['filter'] is not None:  # noqa: E501
            query_params.append(('filter', local_var_params['filter']))  # noqa: E501
        if 'sort_by' in local_var_params and local_var_params['sort_by'] is not None:  # noqa: E501
            query_params.append(('sortBy', local_var_params['sort_by']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'histogram_interval' in local_var_params and local_var_params['histogram_interval'] is not None:  # noqa: E501
            query_params.append(('histogramInterval', local_var_params['histogram_interval']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        header_params['Accept-Encoding'] = "gzip, deflate, br"


        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.0.783'

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        response_types_map = {
            200: "ResourceListWithHistogramOfAccessEvaluationLog",
            400: "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/access', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))
