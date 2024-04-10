import openai

class CodeGenerator:
    def __init__(self, api_key, model="gpt-3.5-turbo", temperature=0.5, max_tokens=150):
        """
        Initialize the code generator with necessary parameters.

        Parameters
        ----------
        api_key : str
            Your OpenAI API key.
        model : str, optional
            The model to use for code generation. Default is 'gpt-3.5-turbo'.
        temperature : float, optional
            Controls randomness in the output. Lower values mean less random outputs.
            Default is 0.5.
        max_tokens : int, optional
            The maximum number of tokens to generate in the output. Default is 150.

        """
        self.api_key = api_key
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        openai.api_key = self.api_key

    def generate_code(self, messages):
        """
        Generate code based on the given messages using OpenAI's API.

        Parameters
        ----------
        messages : list
            List of messages to generate code from.

        Returns
        -------
        str
            Generated code as a string.
        """
        client = openai.Client(api_key=self.api_key)
        response = client.chat.completions.create(
            model=self.model,
            messages=self._create_messages(messages),
        )
        return response.choices[0].message.content
    
    def _create_messages(self, messages):
        """
        Create a list of messages in the format required by OpenAI's API.

        Parameters
        ----------
        messages : list
            List of messages to generate code from.

        Returns
        -------
        list
            List of messages in the required format.
        """
        return [{"role": "user", "content": message.text} for message in messages]