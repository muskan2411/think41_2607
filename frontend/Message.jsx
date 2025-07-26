const Message = ({ message }) => (
  <div className={`my-2 max-w-[70%] px-4 py-2 rounded-lg ${
    message.sender === 'user'
      ? 'bg-blue-600 text-white self-end ml-auto'
      : 'bg-gray-300 text-black self-start'
  }`}>
    {message.text}
  </div>
);

export default Message;
