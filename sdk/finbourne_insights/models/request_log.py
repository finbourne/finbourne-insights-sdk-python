# coding: utf-8

"""
    FINBOURNE Insights API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.807
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from finbourne_insights.configuration import Configuration


class RequestLog(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'timestamp': 'datetime',
        'application': 'str',
        'id': 'str',
        'session_id': 'str',
        'verb': 'str',
        'url': 'str',
        'domain': 'str',
        'user': 'str',
        'user_type': 'str',
        'operation': 'str',
        'outcome': 'str',
        'duration': 'float',
        'http_status_code': 'int',
        'error_code': 'str',
        'sdk_language': 'str',
        'sdk_version': 'str',
        'source_application': 'str',
        'correlation_id': 'list[str]',
        'impersonating_user': 'str',
        'links': 'list[Link]'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'application': 'application',
        'id': 'id',
        'session_id': 'sessionId',
        'verb': 'verb',
        'url': 'url',
        'domain': 'domain',
        'user': 'user',
        'user_type': 'userType',
        'operation': 'operation',
        'outcome': 'outcome',
        'duration': 'duration',
        'http_status_code': 'httpStatusCode',
        'error_code': 'errorCode',
        'sdk_language': 'sdkLanguage',
        'sdk_version': 'sdkVersion',
        'source_application': 'sourceApplication',
        'correlation_id': 'correlationId',
        'impersonating_user': 'impersonatingUser',
        'links': 'links'
    }

    required_map = {
        'timestamp': 'required',
        'application': 'required',
        'id': 'required',
        'session_id': 'optional',
        'verb': 'required',
        'url': 'required',
        'domain': 'optional',
        'user': 'required',
        'user_type': 'optional',
        'operation': 'optional',
        'outcome': 'required',
        'duration': 'required',
        'http_status_code': 'required',
        'error_code': 'optional',
        'sdk_language': 'optional',
        'sdk_version': 'optional',
        'source_application': 'optional',
        'correlation_id': 'optional',
        'impersonating_user': 'optional',
        'links': 'optional'
    }

    def __init__(self, timestamp=None, application=None, id=None, session_id=None, verb=None, url=None, domain=None, user=None, user_type=None, operation=None, outcome=None, duration=None, http_status_code=None, error_code=None, sdk_language=None, sdk_version=None, source_application=None, correlation_id=None, impersonating_user=None, links=None, local_vars_configuration=None):  # noqa: E501
        """RequestLog - a model defined in OpenAPI"
        
        :param timestamp:  The timestamp of the request. (required)
        :type timestamp: datetime
        :param application:  The name of the application that the request was made to. (required)
        :type application: str
        :param id:  The identifier of the request. (required)
        :type id: str
        :param session_id:  The identifier of the session that the request was made in.
        :type session_id: str
        :param verb:  The HTTP verb of the request. (required)
        :type verb: str
        :param url:  The URL of the request. (required)
        :type url: str
        :param domain:  The domain of the request.
        :type domain: str
        :param user:  The user who made the request. (required)
        :type user: str
        :param user_type:  The type of the user who made the request.
        :type user_type: str
        :param operation:  The API operation invoked by the request.
        :type operation: str
        :param outcome:  The outcome of the request: Success, Failure or Error. (required)
        :type outcome: str
        :param duration:  The duration of the request in milliseconds. (required)
        :type duration: float
        :param http_status_code:  The status code of the request. (required)
        :type http_status_code: int
        :param error_code:  Error code, if the request had a failure or error.
        :type error_code: str
        :param sdk_language:  The language of the SDK used.
        :type sdk_language: str
        :param sdk_version:  The version of the SDK used.
        :type sdk_version: str
        :param source_application:  The name of the application that made the request.
        :type source_application: str
        :param correlation_id:  The chain of requestIds preceding this request
        :type correlation_id: list[str]
        :param impersonating_user:  The impersonating user. Only present if the request is an impersonated one
        :type impersonating_user: str
        :param links: 
        :type links: list[finbourne_insights.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._timestamp = None
        self._application = None
        self._id = None
        self._session_id = None
        self._verb = None
        self._url = None
        self._domain = None
        self._user = None
        self._user_type = None
        self._operation = None
        self._outcome = None
        self._duration = None
        self._http_status_code = None
        self._error_code = None
        self._sdk_language = None
        self._sdk_version = None
        self._source_application = None
        self._correlation_id = None
        self._impersonating_user = None
        self._links = None
        self.discriminator = None

        self.timestamp = timestamp
        self.application = application
        self.id = id
        self.session_id = session_id
        self.verb = verb
        self.url = url
        self.domain = domain
        self.user = user
        self.user_type = user_type
        self.operation = operation
        self.outcome = outcome
        self.duration = duration
        self.http_status_code = http_status_code
        self.error_code = error_code
        self.sdk_language = sdk_language
        self.sdk_version = sdk_version
        self.source_application = source_application
        self.correlation_id = correlation_id
        self.impersonating_user = impersonating_user
        self.links = links

    @property
    def timestamp(self):
        """Gets the timestamp of this RequestLog.  # noqa: E501

        The timestamp of the request.  # noqa: E501

        :return: The timestamp of this RequestLog.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this RequestLog.

        The timestamp of the request.  # noqa: E501

        :param timestamp: The timestamp of this RequestLog.  # noqa: E501
        :type timestamp: datetime
        """
        if self.local_vars_configuration.client_side_validation and timestamp is None:  # noqa: E501
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def application(self):
        """Gets the application of this RequestLog.  # noqa: E501

        The name of the application that the request was made to.  # noqa: E501

        :return: The application of this RequestLog.  # noqa: E501
        :rtype: str
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this RequestLog.

        The name of the application that the request was made to.  # noqa: E501

        :param application: The application of this RequestLog.  # noqa: E501
        :type application: str
        """
        if self.local_vars_configuration.client_side_validation and application is None:  # noqa: E501
            raise ValueError("Invalid value for `application`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                application is not None and len(application) < 1):
            raise ValueError("Invalid value for `application`, length must be greater than or equal to `1`")  # noqa: E501

        self._application = application

    @property
    def id(self):
        """Gets the id of this RequestLog.  # noqa: E501

        The identifier of the request.  # noqa: E501

        :return: The id of this RequestLog.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RequestLog.

        The identifier of the request.  # noqa: E501

        :param id: The id of this RequestLog.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                id is not None and len(id) < 1):
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def session_id(self):
        """Gets the session_id of this RequestLog.  # noqa: E501

        The identifier of the session that the request was made in.  # noqa: E501

        :return: The session_id of this RequestLog.  # noqa: E501
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this RequestLog.

        The identifier of the session that the request was made in.  # noqa: E501

        :param session_id: The session_id of this RequestLog.  # noqa: E501
        :type session_id: str
        """

        self._session_id = session_id

    @property
    def verb(self):
        """Gets the verb of this RequestLog.  # noqa: E501

        The HTTP verb of the request.  # noqa: E501

        :return: The verb of this RequestLog.  # noqa: E501
        :rtype: str
        """
        return self._verb

    @verb.setter
    def verb(self, verb):
        """Sets the verb of this RequestLog.

        The HTTP verb of the request.  # noqa: E501

        :param verb: The verb of this RequestLog.  # noqa: E501
        :type verb: str
        """
        if self.local_vars_configuration.client_side_validation and verb is None:  # noqa: E501
            raise ValueError("Invalid value for `verb`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                verb is not None and len(verb) < 1):
            raise ValueError("Invalid value for `verb`, length must be greater than or equal to `1`")  # noqa: E501

        self._verb = verb

    @property
    def url(self):
        """Gets the url of this RequestLog.  # noqa: E501

        The URL of the request.  # noqa: E501

        :return: The url of this RequestLog.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this RequestLog.

        The URL of the request.  # noqa: E501

        :param url: The url of this RequestLog.  # noqa: E501
        :type url: str
        """
        if self.local_vars_configuration.client_side_validation and url is None:  # noqa: E501
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                url is not None and len(url) < 1):
            raise ValueError("Invalid value for `url`, length must be greater than or equal to `1`")  # noqa: E501

        self._url = url

    @property
    def domain(self):
        """Gets the domain of this RequestLog.  # noqa: E501

        The domain of the request.  # noqa: E501

        :return: The domain of this RequestLog.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this RequestLog.

        The domain of the request.  # noqa: E501

        :param domain: The domain of this RequestLog.  # noqa: E501
        :type domain: str
        """

        self._domain = domain

    @property
    def user(self):
        """Gets the user of this RequestLog.  # noqa: E501

        The user who made the request.  # noqa: E501

        :return: The user of this RequestLog.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this RequestLog.

        The user who made the request.  # noqa: E501

        :param user: The user of this RequestLog.  # noqa: E501
        :type user: str
        """
        if self.local_vars_configuration.client_side_validation and user is None:  # noqa: E501
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                user is not None and len(user) < 1):
            raise ValueError("Invalid value for `user`, length must be greater than or equal to `1`")  # noqa: E501

        self._user = user

    @property
    def user_type(self):
        """Gets the user_type of this RequestLog.  # noqa: E501

        The type of the user who made the request.  # noqa: E501

        :return: The user_type of this RequestLog.  # noqa: E501
        :rtype: str
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        """Sets the user_type of this RequestLog.

        The type of the user who made the request.  # noqa: E501

        :param user_type: The user_type of this RequestLog.  # noqa: E501
        :type user_type: str
        """

        self._user_type = user_type

    @property
    def operation(self):
        """Gets the operation of this RequestLog.  # noqa: E501

        The API operation invoked by the request.  # noqa: E501

        :return: The operation of this RequestLog.  # noqa: E501
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this RequestLog.

        The API operation invoked by the request.  # noqa: E501

        :param operation: The operation of this RequestLog.  # noqa: E501
        :type operation: str
        """

        self._operation = operation

    @property
    def outcome(self):
        """Gets the outcome of this RequestLog.  # noqa: E501

        The outcome of the request: Success, Failure or Error.  # noqa: E501

        :return: The outcome of this RequestLog.  # noqa: E501
        :rtype: str
        """
        return self._outcome

    @outcome.setter
    def outcome(self, outcome):
        """Sets the outcome of this RequestLog.

        The outcome of the request: Success, Failure or Error.  # noqa: E501

        :param outcome: The outcome of this RequestLog.  # noqa: E501
        :type outcome: str
        """
        if self.local_vars_configuration.client_side_validation and outcome is None:  # noqa: E501
            raise ValueError("Invalid value for `outcome`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                outcome is not None and len(outcome) < 1):
            raise ValueError("Invalid value for `outcome`, length must be greater than or equal to `1`")  # noqa: E501

        self._outcome = outcome

    @property
    def duration(self):
        """Gets the duration of this RequestLog.  # noqa: E501

        The duration of the request in milliseconds.  # noqa: E501

        :return: The duration of this RequestLog.  # noqa: E501
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this RequestLog.

        The duration of the request in milliseconds.  # noqa: E501

        :param duration: The duration of this RequestLog.  # noqa: E501
        :type duration: float
        """
        if self.local_vars_configuration.client_side_validation and duration is None:  # noqa: E501
            raise ValueError("Invalid value for `duration`, must not be `None`")  # noqa: E501

        self._duration = duration

    @property
    def http_status_code(self):
        """Gets the http_status_code of this RequestLog.  # noqa: E501

        The status code of the request.  # noqa: E501

        :return: The http_status_code of this RequestLog.  # noqa: E501
        :rtype: int
        """
        return self._http_status_code

    @http_status_code.setter
    def http_status_code(self, http_status_code):
        """Sets the http_status_code of this RequestLog.

        The status code of the request.  # noqa: E501

        :param http_status_code: The http_status_code of this RequestLog.  # noqa: E501
        :type http_status_code: int
        """
        if self.local_vars_configuration.client_side_validation and http_status_code is None:  # noqa: E501
            raise ValueError("Invalid value for `http_status_code`, must not be `None`")  # noqa: E501

        self._http_status_code = http_status_code

    @property
    def error_code(self):
        """Gets the error_code of this RequestLog.  # noqa: E501

        Error code, if the request had a failure or error.  # noqa: E501

        :return: The error_code of this RequestLog.  # noqa: E501
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this RequestLog.

        Error code, if the request had a failure or error.  # noqa: E501

        :param error_code: The error_code of this RequestLog.  # noqa: E501
        :type error_code: str
        """

        self._error_code = error_code

    @property
    def sdk_language(self):
        """Gets the sdk_language of this RequestLog.  # noqa: E501

        The language of the SDK used.  # noqa: E501

        :return: The sdk_language of this RequestLog.  # noqa: E501
        :rtype: str
        """
        return self._sdk_language

    @sdk_language.setter
    def sdk_language(self, sdk_language):
        """Sets the sdk_language of this RequestLog.

        The language of the SDK used.  # noqa: E501

        :param sdk_language: The sdk_language of this RequestLog.  # noqa: E501
        :type sdk_language: str
        """

        self._sdk_language = sdk_language

    @property
    def sdk_version(self):
        """Gets the sdk_version of this RequestLog.  # noqa: E501

        The version of the SDK used.  # noqa: E501

        :return: The sdk_version of this RequestLog.  # noqa: E501
        :rtype: str
        """
        return self._sdk_version

    @sdk_version.setter
    def sdk_version(self, sdk_version):
        """Sets the sdk_version of this RequestLog.

        The version of the SDK used.  # noqa: E501

        :param sdk_version: The sdk_version of this RequestLog.  # noqa: E501
        :type sdk_version: str
        """

        self._sdk_version = sdk_version

    @property
    def source_application(self):
        """Gets the source_application of this RequestLog.  # noqa: E501

        The name of the application that made the request.  # noqa: E501

        :return: The source_application of this RequestLog.  # noqa: E501
        :rtype: str
        """
        return self._source_application

    @source_application.setter
    def source_application(self, source_application):
        """Sets the source_application of this RequestLog.

        The name of the application that made the request.  # noqa: E501

        :param source_application: The source_application of this RequestLog.  # noqa: E501
        :type source_application: str
        """

        self._source_application = source_application

    @property
    def correlation_id(self):
        """Gets the correlation_id of this RequestLog.  # noqa: E501

        The chain of requestIds preceding this request  # noqa: E501

        :return: The correlation_id of this RequestLog.  # noqa: E501
        :rtype: list[str]
        """
        return self._correlation_id

    @correlation_id.setter
    def correlation_id(self, correlation_id):
        """Sets the correlation_id of this RequestLog.

        The chain of requestIds preceding this request  # noqa: E501

        :param correlation_id: The correlation_id of this RequestLog.  # noqa: E501
        :type correlation_id: list[str]
        """

        self._correlation_id = correlation_id

    @property
    def impersonating_user(self):
        """Gets the impersonating_user of this RequestLog.  # noqa: E501

        The impersonating user. Only present if the request is an impersonated one  # noqa: E501

        :return: The impersonating_user of this RequestLog.  # noqa: E501
        :rtype: str
        """
        return self._impersonating_user

    @impersonating_user.setter
    def impersonating_user(self, impersonating_user):
        """Sets the impersonating_user of this RequestLog.

        The impersonating user. Only present if the request is an impersonated one  # noqa: E501

        :param impersonating_user: The impersonating_user of this RequestLog.  # noqa: E501
        :type impersonating_user: str
        """

        self._impersonating_user = impersonating_user

    @property
    def links(self):
        """Gets the links of this RequestLog.  # noqa: E501


        :return: The links of this RequestLog.  # noqa: E501
        :rtype: list[finbourne_insights.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this RequestLog.


        :param links: The links of this RequestLog.  # noqa: E501
        :type links: list[finbourne_insights.Link]
        """

        self._links = links

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RequestLog):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RequestLog):
            return True

        return self.to_dict() != other.to_dict()
