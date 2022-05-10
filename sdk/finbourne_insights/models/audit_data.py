# coding: utf-8

"""
    FINBOURNE Insights API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.286
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


class AuditData(object):
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
        'action': 'str',
        'category': 'str',
        'user_id': 'str',
        'message': 'str',
        'resource': 'Resource',
        'details_type': 'str',
        'details': 'object'
    }

    attribute_map = {
        'action': 'action',
        'category': 'category',
        'user_id': 'userId',
        'message': 'message',
        'resource': 'resource',
        'details_type': 'detailsType',
        'details': 'details'
    }

    required_map = {
        'action': 'required',
        'category': 'required',
        'user_id': 'optional',
        'message': 'optional',
        'resource': 'optional',
        'details_type': 'optional',
        'details': 'optional'
    }

    def __init__(self, action=None, category=None, user_id=None, message=None, resource=None, details_type=None, details=None, local_vars_configuration=None):  # noqa: E501
        """AuditData - a model defined in OpenAPI"
        
        :param action:  (required)
        :type action: str
        :param category:  (required)
        :type category: str
        :param user_id: 
        :type user_id: str
        :param message: 
        :type message: str
        :param resource: 
        :type resource: finbourne_insights.Resource
        :param details_type: 
        :type details_type: str
        :param details: 
        :type details: object

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._action = None
        self._category = None
        self._user_id = None
        self._message = None
        self._resource = None
        self._details_type = None
        self._details = None
        self.discriminator = None

        self.action = action
        self.category = category
        self.user_id = user_id
        self.message = message
        if resource is not None:
            self.resource = resource
        self.details_type = details_type
        self.details = details

    @property
    def action(self):
        """Gets the action of this AuditData.  # noqa: E501


        :return: The action of this AuditData.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this AuditData.


        :param action: The action of this AuditData.  # noqa: E501
        :type action: str
        """
        if self.local_vars_configuration.client_side_validation and action is None:  # noqa: E501
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                action is not None and len(action) > 64):
            raise ValueError("Invalid value for `action`, length must be less than or equal to `64`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                action is not None and len(action) < 0):
            raise ValueError("Invalid value for `action`, length must be greater than or equal to `0`")  # noqa: E501

        self._action = action

    @property
    def category(self):
        """Gets the category of this AuditData.  # noqa: E501


        :return: The category of this AuditData.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this AuditData.


        :param category: The category of this AuditData.  # noqa: E501
        :type category: str
        """
        if self.local_vars_configuration.client_side_validation and category is None:  # noqa: E501
            raise ValueError("Invalid value for `category`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                category is not None and len(category) > 16):
            raise ValueError("Invalid value for `category`, length must be less than or equal to `16`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                category is not None and len(category) < 0):
            raise ValueError("Invalid value for `category`, length must be greater than or equal to `0`")  # noqa: E501

        self._category = category

    @property
    def user_id(self):
        """Gets the user_id of this AuditData.  # noqa: E501


        :return: The user_id of this AuditData.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this AuditData.


        :param user_id: The user_id of this AuditData.  # noqa: E501
        :type user_id: str
        """
        if (self.local_vars_configuration.client_side_validation and
                user_id is not None and len(user_id) > 128):
            raise ValueError("Invalid value for `user_id`, length must be less than or equal to `128`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                user_id is not None and len(user_id) < 0):
            raise ValueError("Invalid value for `user_id`, length must be greater than or equal to `0`")  # noqa: E501

        self._user_id = user_id

    @property
    def message(self):
        """Gets the message of this AuditData.  # noqa: E501


        :return: The message of this AuditData.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this AuditData.


        :param message: The message of this AuditData.  # noqa: E501
        :type message: str
        """
        if (self.local_vars_configuration.client_side_validation and
                message is not None and len(message) > 1024):
            raise ValueError("Invalid value for `message`, length must be less than or equal to `1024`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                message is not None and len(message) < 0):
            raise ValueError("Invalid value for `message`, length must be greater than or equal to `0`")  # noqa: E501

        self._message = message

    @property
    def resource(self):
        """Gets the resource of this AuditData.  # noqa: E501


        :return: The resource of this AuditData.  # noqa: E501
        :rtype: finbourne_insights.Resource
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this AuditData.


        :param resource: The resource of this AuditData.  # noqa: E501
        :type resource: finbourne_insights.Resource
        """

        self._resource = resource

    @property
    def details_type(self):
        """Gets the details_type of this AuditData.  # noqa: E501


        :return: The details_type of this AuditData.  # noqa: E501
        :rtype: str
        """
        return self._details_type

    @details_type.setter
    def details_type(self, details_type):
        """Sets the details_type of this AuditData.


        :param details_type: The details_type of this AuditData.  # noqa: E501
        :type details_type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                details_type is not None and len(details_type) > 16):
            raise ValueError("Invalid value for `details_type`, length must be less than or equal to `16`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                details_type is not None and len(details_type) < 0):
            raise ValueError("Invalid value for `details_type`, length must be greater than or equal to `0`")  # noqa: E501

        self._details_type = details_type

    @property
    def details(self):
        """Gets the details of this AuditData.  # noqa: E501


        :return: The details of this AuditData.  # noqa: E501
        :rtype: object
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this AuditData.


        :param details: The details of this AuditData.  # noqa: E501
        :type details: object
        """

        self._details = details

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
        if not isinstance(other, AuditData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AuditData):
            return True

        return self.to_dict() != other.to_dict()
